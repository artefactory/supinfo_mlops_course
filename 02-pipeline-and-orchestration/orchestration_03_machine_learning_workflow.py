import os
import random

import numpy as np
import pickle
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from typing import List
from scipy.sparse import csr_matrix

from prefect import task, flow


########################################
# 1 - Task/FLows tags, version, retries
# 2 - Caching
########################################


@task(retries=3, retry_delay_seconds=60)
def failure():
    print('running')
    if random.randint(1, 10) % 2 == 0:
        raise ValueError("bad code")


@flow()
def test_failure():
    failure()


###################################################
# Workflows orchestration with prefect : EXERCISE 3
###################################################


@task(name='load_data', tags=['preprocessing'], retries=2, retry_delay_seconds=60)
def load_data(path: str):
    return pd.read_parquet(path)


@task(name='compute_duration', tags=['preprocessing'])
def compute_target(
        df: pd.DataFrame,
        pickup_column: str = "tpep_pickup_datetime",
        dropoff_column: str = "tpep_dropoff_datetime"
) -> pd.DataFrame:
    df["duration"] = df[dropoff_column] - df[pickup_column]
    df["duration"] = df["duration"].dt.total_seconds() / 60
    return df


@task(name='filter_outliers', tags=['preprocessing'])
def filter_outliers(
        df: pd.DataFrame,
        min_duration: int = 1,
        max_duration: int = 60
) -> pd.DataFrame:
    return df[df['duration'].between(min_duration, max_duration)]


@task(name='encode_cat_cols', tags=['preprocessing'])
def encode_categorical_cols(
        df: pd.DataFrame,
        categorical_cols: List[str] = None
) -> pd.DataFrame:
    if categorical_cols is None:
        categorical_cols = ['PULocationID', 'DOLocationID', 'passenger_count']
    df[categorical_cols] = df[categorical_cols].fillna(-1).astype('int')
    df[categorical_cols] = df[categorical_cols].astype('str')
    return df


@task(name='extract_x_y', tags=['preprocessing'])
def extract_x_y(
        df: pd.DataFrame,
        categorical_cols: List[str] = None,
        dv: DictVectorizer = None,
        with_target: bool = True
) -> dict:

    if categorical_cols is None:
        categorical_cols = ['PULocationID', 'DOLocationID', 'passenger_count']
    dicts = df[categorical_cols].to_dict(orient='records')

    y = None
    if with_target:
        if dv is None:
            dv = DictVectorizer()
            dv.fit(dicts)
        y = df["duration"].values

    x = dv.transform(dicts)
    return {'x': x, 'y': y, 'dv': dv}


@flow(name="Train processing", retries=1, retry_delay_seconds=30)
def process_train_data(path,  dv=None):
    df = load_data(path)
    df1 = compute_target(df)
    df2 = filter_outliers(df1)
    df3 = encode_categorical_cols(df2)
    return extract_x_y(df3, dv=dv)


@flow(name="Inference Processing", retries=1, retry_delay_seconds=30)
def process_inference_data(path, dv):
    df = load_data(path)
    df1 = encode_categorical_cols(df)
    return extract_x_y(df1, dv=dv, with_target=False)


###################################################
# Workflows orchestration with prefect : EXERCISE 4
###################################################


@task(name="Train model", tags=['Model'])
def train_model(
        x_train: csr_matrix,
        y_train: np.ndarray
):
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    return lr


@task(name="Make prediction", tags=["Model"])
def predict_duration(
        input_data: csr_matrix,
        model: LinearRegression
):
    return model.predict(input_data)


@task(name="Evaluation", tags=["Model"])
def evaluate_model(
        y_true: np.ndarray,
        y_pred: np.ndarray
):
    return mean_squared_error(y_true, y_pred, squared=False)


@task(name="Load", tags=['Serialize'])
def load_pickle(path: str):
    with open(path, 'rb') as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


@task(name="Save", tags=['Serialize'])
def save_pickle(path: str, obj: dict):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


#########################################################
# Typing tasks in prefect is done as with any python code
# For flows, either use `validate_parameters=False`
# or define pydantic models for prefect to understand
# your NON DEFAULT typing. But il all tasks are typed, since flows are
# just set of tasks, it should be all good if we don't
# want to add a layer of complexity
#########################################################


@flow(name="Model initialisation")
def train_and_predict(
        x_train,
        y_train,
        x_test,
        y_test
):
    model = train_model(x_train, y_train)
    prediction = predict_duration(x_test, model)
    mse = evaluate_model(y_test, prediction)
    return {'model': model, 'mse': mse}


@flow(name="Example Machine learning workflow", retries=1, retry_delay_seconds=30)
def complete_ml(
        train_path: str,
        test_path: str,
        save_model: bool = True,
        save_dv: bool = True,
        local_storage: str = "./results"
):
    if not os.path.exists(local_storage):
        os.makedirs(local_storage)

    train_data = process_train_data(train_path)
    test_data = process_train_data(test_path, dv=train_data["dv"])
    model_obj = train_and_predict(train_data["x"], train_data["y"], test_data['x'], test_data['y'])
    if save_model:
        save_pickle(f"{local_storage}/model.pickle", model_obj)
    if save_dv:
        save_pickle(f"{local_storage}/dv.pickle", train_data["dv"])


@flow(name="Batch inference", retries=1, retry_delay_seconds=30)
def batch_inference(input_path, dv=None, model=None, local_storage='./results'):

    if not dv:
        dv = load_pickle(f"{local_storage}/dv.pickle")
    data = process_inference_data(input_path, dv)

    if not model:
        model = load_pickle(f"{local_storage}/model.pickle")["model"]
    return predict_duration(data["x"], model)


if __name__ == "__main__":

    train_path = "../00-data/yellow_tripdata_2021-01.parquet"
    test_path = "../00-data/yellow_tripdata_2021-02.parquet"
    inference_path = "../00-data/yellow_tripdata_2021-02.parquet"

    complete_ml(train_path, test_path)
    inference = batch_inference(inference_path)


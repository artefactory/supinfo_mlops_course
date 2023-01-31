import os
import numpy as np
import pickle
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from typing import List
from scipy.sparse import csr_matrix


##########
# HELPERS
##########

def load_pickle(path: str):
    with open(path, 'rb') as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


def save_pickle(path: str, obj: dict):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)


###########################################
# FROM NOTEBOOKS TO WORKFLOWS : EXERCISE 1
###########################################


def load_data(path: str):
    return pd.read_parquet(path)


def compute_target(
        df: pd.DataFrame,
        pickup_column: str = "tpep_pickup_datetime",
        dropoff_column: str = "tpep_dropoff_datetime"
) -> pd.DataFrame:
    df["duration"] = df[dropoff_column] - df[pickup_column]
    df["duration"] = df["duration"].dt.total_seconds() / 60
    return df


def filter_outliers(
        df: pd.DataFrame,
        min_duration: int = 1,
        max_duration: int = 60
) -> pd.DataFrame:
    return df[df['duration'].between(min_duration, max_duration)]


def encode_categorical_cols(
        df: pd.DataFrame,
        categorical_cols: List[str] = None
) -> pd.DataFrame:
    if categorical_cols is None:
        categorical_cols = ['PULocationID', 'DOLocationID', 'passenger_count']
    df[categorical_cols] = df[categorical_cols].fillna(-1).astype('int')
    df[categorical_cols] = df[categorical_cols].astype('str')
    return df


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


###########################################
# FROM NOTEBOOKS TO WORKFLOWS : EXERCISE 2
###########################################


def process_data(path: str,  dv=None, with_target: bool = True):
    df = load_data(path)
    if with_target:
        df1 = compute_target(df)
        df2 = filter_outliers(df1)
        df3 = encode_categorical_cols(df2)
        return extract_x_y(df3, dv=dv)
    else:
        df1 = encode_categorical_cols(df)
        return extract_x_y(df1, dv=dv, with_target=with_target)


###########################################
# FROM NOTEBOOKS TO WORKFLOWS : EXERCISE 3
###########################################

# Functions ###

def train_model(
        x_train: csr_matrix,
        y_train: np.ndarray
):
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    return lr


def predict_duration(
        input_data: csr_matrix,
        model: LinearRegression
):
    return model.predict(input_data)


def evaluate_model(
        y_true: np.ndarray,
        y_pred: np.ndarray
):
    return mean_squared_error(y_true, y_pred, squared=False)


# Entrypoints ###

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


def complete_ml(
        train_path: str,
        test_path: str,
        save_model: bool = True,
        save_dv: bool = True,
        local_storage: str = "./results"
):
    if not os.path.exists(local_storage):
        os.makedirs(local_storage)

    train_data = process_data(train_path)
    test_data = process_data(test_path, dv=train_data["dv"])
    model_obj = train_and_predict(train_data["x"], train_data["y"], test_data['x'], test_data['y'])
    if save_model:
        save_pickle(f"{local_storage}/model.pickle", model_obj)
    if save_dv:
        save_pickle(f"{local_storage}/dv.pickle", train_data["dv"])


def batch_inference(input_path, dv=None, model=None, local_storage='./results'):
    if not dv:
        dv = load_pickle(f"{local_storage}/dv.pickle")
    data = process_data(input_path, dv, with_target=False)
    if not model:
        model = load_pickle(f"{local_storage}/model.pickle")["model"]
    return predict_duration(data["x"], model)


if __name__ == "__main__":

    train_path = "../00-data/yellow_tripdata_2021-01.parquet"
    test_path = "../00-data/yellow_tripdata_2021-02.parquet"
    inference_path = "../00-data/yellow_tripdata_2021-02.parquet"

    complete_ml(train_path, test_path)
    inference = batch_inference(inference_path)

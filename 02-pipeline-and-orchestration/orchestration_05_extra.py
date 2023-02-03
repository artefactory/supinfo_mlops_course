import time
from prefect import task, flow
from prefect.task_runners import SequentialTaskRunner


#####################################
# Prefect Typing with pydantic models
#####################################

import numpy as np
from pydantic import BaseModel, validator
from scipy.sparse import csr_matrix
from sklearn.feature_extraction import DictVectorizer

from orchestration_03_machine_learning_workflow import (
    train_model,
    predict_duration,
    evaluate_model
)

from orchestration_03_machine_learning_workflow import (
    load_data,
    compute_target,
    filter_outliers,
    encode_categorical_cols,
    extract_x_y
)


class Data(BaseModel):

    """
    Defines pydantic validators for custom types
    In this validators, a test is made on the shape.
    But a lot of other things can also be done to validate
    """

    x_train: csr_matrix = None
    x_test: csr_matrix = None
    y_train: np.ndarray = None
    y_test: np.ndarray = None
    dv: DictVectorizer = None

    @validator("x_train", "x_test")
    def check_x_type(cls, value):
        if not value.get_shape()[1] == 528:
            raise ValueError("Incorrect Type")
        return value

    class Config:
        arbitrary_types_allowed = True


@flow(name="Train processing", retries=1, retry_delay_seconds=30)
def process_train_data(path: str,  data_object: Data = Data()):
    df = load_data(path)
    df1 = compute_target(df)
    df2 = filter_outliers(df1)
    df3 = encode_categorical_cols(df2)
    return extract_x_y(df3, dv=data_object.dv)


@flow(name="Model initialisation")
def train_and_predict(data_object: Data):
    model = train_model(data_object.x_train, data_object.y_train)
    prediction = predict_duration(data_object.x_test, model)
    mse = evaluate_model(data_object.y_test, prediction)
    return {'model': model, 'mse': mse}


#####################################
# Prefect Task runners basic example
#####################################


@task
def print_values(values):
    for value in values:
        time.sleep(1)
        print(value)
        print(value, end="\r")


@flow
def concurrent_flow():
    print_values(["Task A"] * 15)
    print_values(["Task B"] * 10)


@flow(task_runner=SequentialTaskRunner())
def sequential_flow():
    print_values(["Task A"] * 15)
    print_values(["Task B"] * 10)

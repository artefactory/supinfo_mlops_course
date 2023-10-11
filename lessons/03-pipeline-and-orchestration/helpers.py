import pickle
import random

from prefect import flow, task


def load_pickle(path: str):
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


def save_pickle(path: str, obj: dict):
    with open(path, "wb") as f:
        pickle.dump(obj, f)


@task(retries=3, retry_delay_seconds=60)
def failure():
    print("running")
    if random.randint(1, 10) % 2 == 0:
        raise ValueError("This number is not even")


@flow()
def test_failure():
    failure()


@task(name="Load", tags=["Serialize"])
def task_load_pickle(path: str):
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


@task(name="Save", tags=["Serialize"])
def task_save_pickle(path: str, obj: dict):
    with open(path, "wb") as f:
        pickle.dump(obj, f)

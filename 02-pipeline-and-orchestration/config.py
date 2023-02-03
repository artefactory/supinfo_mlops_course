import os

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DATA_DIR = os.path.join(BASE_PATH, "00-data")
LOCAL_STORAGE = os.path.join(BASE_PATH, "02-pipeline-and-orchestration/results")
TRAIN_DATA = os.path.join(BASE_PATH, "00-data/yellow_tripdata_2021-01.parquet")
TEST_DATA = os.path.join(BASE_PATH, "00-data/yellow_tripdata_2021-02.parquet")
INFERENCE_DATA = os.path.join(BASE_PATH, "00-data/yellow_tripdata_2021-03.parquet")
CATEGORICAL_VARS = ['PULocationID', 'DOLocationID', 'passenger_count']

import logging
from pathlib import Path

import pandas as pd


def get_logger(logging_level=logging.INFO, logger_name: str = "model_deployment_logger"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging_level)
    ch = logging.StreamHandler()
    ch.setLevel(logging_level)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


def is_docker() -> bool:
    cgroup = Path("/proc/self/cgroup")
    return Path("/.dockerenv").is_file() or cgroup.is_file() and cgroup.read_text().find("docker") > -1


# LOGGING
LOGGER_LEVEL = "INFO"
logger = get_logger(logging_level=getattr(logging, LOGGER_LEVEL))

# PATHS
ROOT_DIR = Path(__file__).parent
PATH_LOCAL_DATA = ROOT_DIR / "local_data"
PATH_LOCAL_MODELS = ROOT_DIR / "web_service/local_models"

# DATA
TRAIN_DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
PATH_TRAIN_DATA = PATH_LOCAL_DATA / "yellow_tripdata_2021-01.parquet"

TEST_DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-02.parquet"
PATH_TEST_DATA = PATH_LOCAL_DATA / "yellow_tripdata_2021-02.parquet"

INFERENCE_DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-03.parquet"
PATH_INFERENCE_DATA = PATH_LOCAL_DATA / "yellow_tripdata_2021-03.parquet"

# MISC
CATEGORICAL_VARS = ["PULocationID", "DOLocationID", "passenger_count"]
MODEL_VERSION = "0.0.1"

# MLFLOW
MLFLOW_TRACKING_URI = "http://mlflow:5000" if is_docker() else "http://localhost:5000"
MLFLOW_EXPERIMENT_NAME = "trip_duration_prediction"
REGISTERED_MODEL_NAME = "trip_duration_model"

# silence pandas `SettingWithCopyWarning` warnings
pd.options.mode.chained_assignment = None  # default='warn'

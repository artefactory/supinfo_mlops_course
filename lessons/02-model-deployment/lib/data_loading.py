from urllib import request

import pandas as pd
from config import logger


def download_data_from_url(url: str, local_output_path: str):
    logger.info(f"Downloading data from {url} to {local_output_path}...")
    request.urlretrieve(url, filename=local_output_path)
    logger.info("Done.\n")


def load_data(path: str) -> pd.DataFrame:
    logger.info(f"Loading data from {path}")
    return pd.read_parquet(path)

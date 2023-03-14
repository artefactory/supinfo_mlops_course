import joblib

from app_config import logger


def load_pipeline(path: str):
    logger.info(f"Loading pipeline from {path}")
    return joblib.load(path)

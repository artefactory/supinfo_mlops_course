import joblib

from config import logger


def save_pipeline(pipeline, path: str):
    logger.info(f"Saving pipeline to {path}")
    joblib.dump(pipeline, path)


def load_pipeline(path: str):
    logger.info(f"Loading pipeline from {path}")
    return joblib.load(path)

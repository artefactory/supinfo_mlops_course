from typing import List

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline, make_pipeline

from config import logger


def fit_pipeline(feature_dicts: List[dict], target: pd.Series) -> Pipeline:
    """Fit a pipeline that transforms a list of dicts into a s
       parse matrix and then fits a linear regression model
    """
    logger.info("Fitting pipeline...")
    pipeline = make_pipeline(DictVectorizer(), LinearRegression(), verbose=True)
    pipeline.fit(feature_dicts, target)
    return pipeline


def predict_pipeline(pipeline: Pipeline, feature_dicts: List[dict]) -> pd.Series:
    """Use a fitted pipeline to make predictions"""
    logger.info("Making predictions...")
    predictions = pipeline.predict(feature_dicts)
    return predictions


def compute_rmse(target: pd.Series, predictions: pd.Series) -> None:
    """Evaluate a fitted pipeline using root mean squared error"""
    logger.info("Computing RMSE...")
    return mean_squared_error(target, predictions, squared=False)

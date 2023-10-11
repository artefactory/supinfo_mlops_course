from typing import List, Union

import pandas as pd
from config import CATEGORICAL_VARS, logger


def _compute_target(
    df: pd.DataFrame,
    pickup_column: str = "tpep_pickup_datetime",
    dropoff_column: str = "tpep_dropoff_datetime",
) -> pd.DataFrame:
    """
    Compute the trip duration in minutes based
    on pickup and dropoff time
    """
    logger.info("Computing target...")
    df["duration"] = df[dropoff_column] - df[pickup_column]
    df["duration"] = df["duration"].dt.total_seconds() / 60
    return df


def _filter_outliers(df: pd.DataFrame, min_duration: int = 1, max_duration: int = 60) -> pd.DataFrame:
    """
    Remove rows corresponding to negative/zero
    and too high target' values from the dataset
    """
    logger.info("Filtering outliers...")
    return df[df["duration"].between(min_duration, max_duration)]


def _encode_categorical_cols(df: pd.DataFrame, categorical_cols: List[str] = None) -> pd.DataFrame:
    """
    Takes a Pandas dataframe and a list of categorical
    column names, and returns dataframe with
    the specified columns converted to categorical data type
    """
    logger.info("Encoding categorical columns...")
    if categorical_cols is None:
        categorical_cols = CATEGORICAL_VARS
    df[categorical_cols] = df[categorical_cols].fillna(-1).astype("int")
    df[categorical_cols] = df[categorical_cols].astype("category")
    return df


def prepare_data(
    data: Union[pd.DataFrame, dict],
    target_col: str = "duration",
    categorical_cols: list = CATEGORICAL_VARS,
) -> tuple:
    """Prepare data for training or prediction
    Args:
        data (Union[pd.DataFrame, dict]): data to prepare, dict when online inference.
        target_col (str, optional): Target column name. Defaults to "duration".
        categorical_cols (list, optional): Categorical column names list. Defaults to CATEGORICAL_VARS.

    Returns:
        tuple: (feature_dicts, target)
    """
    logger.info("Pre-processing data...")
    if isinstance(data, pd.DataFrame):
        data = data.copy(deep=True)
        data = _compute_target(data)
        data = _filter_outliers(data)
        data = _encode_categorical_cols(data, categorical_cols=categorical_cols)
        target = data[target_col]
    elif isinstance(data, dict):
        data = _encode_categorical_cols(pd.DataFrame([data]), categorical_cols=categorical_cols)
        target = None
    feature_dicts = data[categorical_cols].to_dict(orient="records")
    return feature_dicts, target

from typing import List

import pandas as pd
from app_config import CATEGORICAL_VARS, logger


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


def prepare_data(data: dict, categorical_cols: list = CATEGORICAL_VARS) -> tuple:
    """Prepare data for training or prediction
    Args:
        data (dict): data to prepare.
        categorical_cols (list, optional): Categorical column names list. Defaults to CATEGORICAL_VARS.

    Returns:
        tuple: feature_dicts
    """
    logger.info("Pre-processing data...")
    if isinstance(data, dict):
        data = _encode_categorical_cols(pd.DataFrame([data]), categorical_cols=categorical_cols)
    else:
        raise ValueError("Input data must be or a dictionary")
    feature_dicts = data[categorical_cols].to_dict(orient="records")
    return feature_dicts

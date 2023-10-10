from sklearn.pipeline import Pipeline
from lib.preprocessing import prepare_data

from app_config import logger


def run_inference(payload: dict,
                  pipeline: Pipeline) -> float:
    """
    Takes a pre-fitted pipeline (dictvectorizer + linear regression model)
    outputs the computed trip duration in minutes.
    example payload:
        {'PULocationID': 264, 'DOLocationID': 264, 'passenger_count': 1}
    """
    logger.info("Running inference on payload...")
    prep_features = prepare_data(payload)
    trip_duration_prediction = pipeline.predict(prep_features)[0]
    return trip_duration_prediction

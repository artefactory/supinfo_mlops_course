import mlflow
from config import (
    MLFLOW_EXPERIMENT_NAME,
    MLFLOW_TRACKING_URI,
    PATH_TEST_DATA,
    PATH_TRAIN_DATA,
    REGISTERED_MODEL_NAME,
    logger,
)
from lib.data_loading import load_data
from lib.modelling import compute_rmse, fit_pipeline, predict_pipeline
from lib.preprocessing import prepare_data

if __name__ == "__main__":
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
    mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)

    with mlflow.start_run() as run:
        run_id = run.info.run_id
        logger.info(f"run id: {run_id}")
        logger.info(f"artifact_uri: {mlflow.get_artifact_uri()}")
        logger.info(f"registry_uri: {mlflow.get_registry_uri()}")

        train_data = load_data(path=PATH_TRAIN_DATA)
        test_data = load_data(path=PATH_TEST_DATA)

        train_feature_dicts, train_target = prepare_data(train_data)
        test_feature_dicts, test_target = prepare_data(test_data)

        pipeline = fit_pipeline(train_feature_dicts, train_target)
        predictions = predict_pipeline(pipeline, test_feature_dicts)
        rmse = compute_rmse(test_target, predictions)
        logger.info(f"RMSE: {rmse}")

        params = {
            "model_type": pipeline.steps[1][1].__class__.__name__,
            "preprocessing_type": pipeline.steps[0][1].__class__.__name__,
        }
        mlflow.log_params(params)
        mlflow.log_metric("test_rmse", rmse)
        logger.info(f"Logging and register the model {REGISTERED_MODEL_NAME}...")
        mlflow.sklearn.log_model(pipeline, artifact_path="model", registered_model_name=REGISTERED_MODEL_NAME)

    # Trasition model to production
    logger.info(f"Transition model {REGISTERED_MODEL_NAME} to production...")
    client = mlflow.MlflowClient()
    client.transition_model_version_stage(name=REGISTERED_MODEL_NAME, version=1, stage="Production")

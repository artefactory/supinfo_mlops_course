from config import PATH_TRAIN_DATA, PATH_TEST_DATA, PATH_LOCAL_MODELS, MODEL_VERSION, logger
from lib.preprocessing import prepare_data
from lib.data_loading import load_data
from lib.modelling import fit_pipeline, predict_pipeline, compute_rmse
from lib.utils import save_pipeline


if __name__ == "__main__":
    train_data = load_data(path=PATH_TRAIN_DATA)
    test_data = load_data(path=PATH_TEST_DATA)
    train_feature_dicts, train_target = prepare_data(train_data)
    test_feature_dicts, test_target = prepare_data(test_data)
    pipeline = fit_pipeline(train_feature_dicts, train_target)
    predictions = predict_pipeline(pipeline, test_feature_dicts)
    rmse = compute_rmse(test_target, predictions)
    logger.info(f"RMSE: {rmse}")
    output_pipeline_path = f"{PATH_LOCAL_MODELS}/pipeline__v{MODEL_VERSION}.joblib"
    save_pipeline(pipeline, path=output_pipeline_path)

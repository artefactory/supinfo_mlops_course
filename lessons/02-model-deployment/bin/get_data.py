from lib.data_loading import download_data_from_url
from config import (INFERENCE_DATA_URL, PATH_INFERENCE_DATA,
                    TRAIN_DATA_URL, PATH_TRAIN_DATA,
                    TEST_DATA_URL, PATH_TEST_DATA)


if __name__ == "__main__":
    # train data
    download_data_from_url(
        url=TRAIN_DATA_URL,
        local_output_path=PATH_TRAIN_DATA,
    )

    # test data
    download_data_from_url(
        url=TEST_DATA_URL,
        local_output_path=PATH_TEST_DATA,
    )

    # inference data
    download_data_from_url(
        url=INFERENCE_DATA_URL,
        local_output_path=PATH_INFERENCE_DATA,
    )

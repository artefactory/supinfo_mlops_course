import requests
from requests.exceptions import HTTPError

from config import logger


def post_payload(url: str, payload: dict):
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response: \n{response.json()}")
    except HTTPError as e:
        logger.error(f"Error: {e}")
        raise e


if __name__ == "__main__":
    example_payload = {"PULocationID": 264, "DOLocationID": 264, "passenger_count": 1}
    url = "http://localhost:8001/predict"
    # if you are running the web_service locally, use the following url: "http://localhost:8000/predict"
    response = post_payload(url=url, payload=example_payload)

    # equivalent to a curl command:
    # curl -X POST 'http://localhost:8000/predict' \
    #   -H 'accept: application/json' \
    #   -H 'Content-Type: application/json' \
    #   -d '{"PULocationID": 264,  "DOLocationID": 264,  "passenger_count": 1}'

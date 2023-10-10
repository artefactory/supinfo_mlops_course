from fastapi import FastAPI
from pydantic import BaseModel

from lib.modelling import run_inference
from lib.utils import load_pipeline
from app_config import (MODEL_VERSION, APP_TITLE, APP_DESCRIPTION, APP_VERSION,
                        PATH_TO_PIPELINE)


app = FastAPI(title=APP_TITLE,
              description=APP_DESCRIPTION,
              version=APP_VERSION)


class InputData(BaseModel):
    PULocationID: int
    DOLocationID: int
    passenger_count: int


class PredictionOut(BaseModel):
    trip_duration_prediction: float


pipeline = load_pipeline(PATH_TO_PIPELINE)


@app.get("/")
def home():
    return {"health_check": "OK",
            "model_version": MODEL_VERSION}


@app.post("/predict", response_model=PredictionOut, status_code=201)
def predict(payload: InputData):
    trip_duration_prediction = run_inference(payload.dict(), pipeline)
    return {"trip_duration_prediction": trip_duration_prediction}

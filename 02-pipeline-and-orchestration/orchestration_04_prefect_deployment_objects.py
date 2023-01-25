from orchestration_03_machine_learning_workflow import complete_ml
from orchestration_03_machine_learning_workflow import batch_inference

from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import (
   CronSchedule,
   IntervalSchedule,
)


modeling_deployment_every_sunday = Deployment.build_from_flow(
    name="Model training Deployment",
    flow=complete_ml,
    version="1.0",
    tags=["model"],
    schedule=CronSchedule(cron="0 0 * * 0")
)


inference_deployment_every_minute = Deployment.build_from_flow(
    name="Model Inference Deployment",
    flow=batch_inference,
    version="1.0",
    tags=["inference"],
    schedule=IntervalSchedule(interval=600)
)


if __name__ == "__main__":

    modeling_deployment_every_sunday.apply()
    inference_deployment_every_minute.apply()

    train_path = "../00-data/yellow_tripdata_2021-01.parquet"
    test_path = "../00-data/yellow_tripdata_2021-02.parquet"
    inference_path = "../00-data/yellow_tripdata_2021-02.parquet"

    complete_ml(train_path, test_path)
    inference = batch_inference(inference_path)


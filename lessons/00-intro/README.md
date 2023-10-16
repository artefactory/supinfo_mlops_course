## Introduction and Use Case Reminder

The project focuses on predicting the duration of *New York City Taxi trips*. \
The objective is to use the available data to train a simple machine learning model
that can predict the trip duration based on inputs that could be available in a production environment.

The ultimate goal for this use case could be to predict trip durations in real time (similar to Google Maps or Waze itineraries),
but for simplicity, in this module, we will assume that we only need batch predictions. The data for which we need predictions
will be stored in a file for ingestion by an untrained model.

The machine learning phase primarily consists of the following steps:
- Data processing
- Model training
- Model evaluation
- Prediction

The data for this module can be downloaded from the [TLC Trip Record Data page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
To complete this module, you will need three samples of data:
- `Sample 1 example`: [Yellow trip 2021-01 data](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet) (for model training)
- `Sample 2 example`: [Yellow trip 2021-02 data](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-02.parquet) (for model evaluation)
- `Sample 3 example`: [Yellow trip 2021-03 data](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-03.parquet) (for prediction)

> **Disclaimer** :
> The volumes of data used in this module are not significant enough to produce efficient models and
interpretable performances. Here we use data volumes that fit locally and allow for pipeline building and fast execution, but we do not focus on model performance and interpretability as it is not the main focus of this course.

> **Data location** :
> Please create a "00-data" folder in the course root directory and place the downloaded files inside. \
> If the names are different, please rename your files to "yellow_tripdata_2021-01.parquet", "yellow_tripdata_2021-02.parquet", and "yellow_tripdata_2021-03.parquet" respectively.

## Notebook Execution

A notebook implementing the machine learning steps to predict Taxi trip duration can be found in the
course's GitHub repository in the [introduction course](https://github.com/artefactory/supinfo_mlops_course/blob/master/lessons/01-intro).

Since the main focus of the course is not Machine Learning itself, we recommend running the notebook in your local Jupyter container.

1. First, let's create our Jupyter Lab image and network by running
```bash
make prepare-mlops-crashcourse
```

2. Then, let's create our local Jupyter Lab container by running
```bash
make launch-mlops-crashcourse
```
You will need to pass the token 'MLOPS' to your Jupyter Lab UI

3. Finally, navigate to `lessons/01-intro/practice-intro-supinfo.ipynb` and try running and understanding the model implementation

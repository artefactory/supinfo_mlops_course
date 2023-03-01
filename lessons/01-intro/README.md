## Intro and Use case Reminder

The project is *New York City Taxi trip duration prediction*. \
The goal is to use the available data in order to train a simple machine learning model
to predict the trip duration based on some input that can be available in production environment.

An ultimate goal for this use case can be to predict in real time trips durations (google-maps/waze like itinerary)
but for simplicity, in this module, we assume that we need batch prediction. The data for which we need predictions
will be stored in a file for ingestion in the trained model.

The machine learning phase is mainly constituted by the following steps : 
- data processing
- model training
- model evaluation
- prediction

The data to use for this module can be downloaded from the [TLC Trip Record Data page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page).
To complete this module, you will need 03 samples of data :
- `sample 1 example` : [yellow trip 2021-01 data](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet) (to train model)
- `sample 2 example` : [yellow trip 2021-02 data](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-02.parquet) (to evaluate model)
- `sample 3 example` : [yellow trip 2021-03 data](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-03.parquet) (for prediction)

> **Disclaimer** :
> The volumes of data used in this module are not at all significant to have efficient models and 
interpretable performances. Here we use data volumes that fit locally and allow pipelines building and fast execution but we don't focus on model performance and interpretability because it is not the main focus of this course.

> **Data location** :
> Please create a "00-data" folder in the course root directory and put the downloaded files inside. \
> If names are different, please rename your files to "yellow_tripdata_2021-01.parquet" (2021-02 / 2021-03)

## Notebook execution

A notebook implementing the machine learning steps to predict Taxi trip duration can be found in the 
course' GitHub repository in the [introduction course](https://github.com/artefactory/supinfo_mlops_course/blob/master/lessons/01-intro).

Since the main focus of the course is not Machine Learning itself, let's just run the notebook in your local jupyter container.

#TODO: put clear instructions

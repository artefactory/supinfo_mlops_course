## Machine learning pipelines and Orchestration

> **Version**
> This module has been created using Prefect 2.7.9

### Intro and Use case Reminder

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
- `sample 1 example` : yellow trip 2021-01 data (to train model)
- `sample 2 example` : yellow trip 2021-02 data (to evaluate model)
- `sample 3 example` : yellow trip 2021-03 data (for prediction)

A notebook implementing the machine learning steps to predict Taxi trip duration can be found in the 
course' GitHub repository in the [introduction course](https://github.com/artefactory/supinfo_mlops_course/tree/master/01-intro).

### From notebook to Workflows :
#### *e.g. solution : orchestration_00_machine_learning.py*

First step before using prefect for orchestration is to transform our notebook into python files 
following known good practices.

**Exercise 1** : Convert notebook into python files (1/3)

Create/move the following functions in/to a file using the notebook's code and applying good code practices viewed :
- load_data
- compute_target
- filter_outliers
- encode_categorical_columns
- extract_x_y

**Exercise 2** : Convert notebook into python files (2/3) 

These steps constitute the data processing phase. \
Create two `processing` functions as entrypoint for all these steps

- The first use all steps to `process_train_data`
- The second don't compute target or filter outliers and will be used to `process_prediction_data` to predict in "production".

The extract return `x`, `y` and `dv`. \
The `dv` from `process_train_data` should be used as argument in `process_prediction_data` to transform the test data


**Exercise 3**: Convert notebook into python files (3/3)

Create five functions to complete the ML process : 
- train model
- evaluate model
- predict
- An entrypoint function to perform all the previous steps  for training phase:
  - process train data
  - train model
  - evaluate model
- An entrypoint function for prediction:
  - process prediction data
  - predict
- Test your code with the downloaded data

Hint : Add a save step using helpers, at the end of the ml pipeline to serialize your model and dict vectorizer.
These two element will be loaded for batch prediction.


### Workflows orchestration with prefect : 

#### e.g. solutions : 
- *exercise 1 : orchestration_01_prefect_orion.sh*
- *exercise 2 : orchestration_02_first_flow.py*
- *exercise 3 : orchestration_03_machine_learning_workflow.py*
- *exercise 4 : orchestration_03_machine_learning_workflow.py*
- *exercise 5 : orchestration_04_prefect_deployment_objects.py*

Helpers : 
```
@task(name="Load", tags=['Serialize'])
def load_pickle(path: str):
    with open(path, 'rb') as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


@task(name="Save", tags=['Serialize'])
def save_pickle(path: str, obj: dict):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)
```


**Exercise 1**: Set Up Prefect UI

Before starting to implement tasks and flows with prefect, let's set up the UI in order to have a good visualization
of our work.

Steps : 
- Start a local prefect server : `prefect orion start`
- Set an API URL for your local server to make sure that your workflow will be tracked by this specific instance : `prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api`

Prefect database is stored at `~/.prefect/orion.db`
If you want to reset the database, run `prefect orion database reset`

**Exercise 2**: Create a data processing flow

Import flow and task object from prefect.
- Use the decorators `@task` and `@flow` to create your first prefect flows :
  - processing train data
  - processing prediction data
- Test your code by calling the flows run with downloaded data
- Visualize in the local prefect UI

> :warning: **Typing tasks and flows in prefect** : \
Typing tasks in prefect is done as with any python code. \
For flows, either use `validate_parameters=False`
or define pydantic models for prefect to understand
your NON DEFAULT typing (see extra section). \

> But if all tasks are typed, since flows are just set of tasks, it should be all good if we don't want to add a layer of complexity \
> `Default types` : str, int ...


**Exercise 3**: Customize your flows

You can configure the property and special behavior for your prefect tasks/flow in the decorator.
For example, you can tell if you want to retry on a failure, set name or tags, etc...
```
@task('name=failure_task', tags=['fails'], retries=3, retry_delay_seconds=60)
def failure():
    print('running')
    if random.randint(1, 10) % 2 == 0:
        raise ValueError("bad code")

@flow(name='failure_flow', version='1.0')
def test_failure():
    failure()
```

- Add names, tasks, and desired behavior to your tasks/flows
- Test your code
- Visualize in the local prefect UI

 
**Exercise 4** : Create machine learning flows

Create the complete ML process flow : 
- process train data
- train model
- evaluate model
- save model and vectorizer (dv) | use helpers
- predict 

Create the prediction flow:
- load model and vectorizer
- process prediction data
- predict

- Test your code
- Visualize in the UI


**Exercise 5** : Create flows deployments with prefect

Helper example :

```
from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import (
   CronSchedule,
   IntervalSchedule,
)

shcedule_examples = [
    IntervalSchedule(interval=600)
    CronSchedule(cron="0 0 * * 0")
] 

dep = Deployment.build_from_flow(
    name="<random name>",
    flow=<existing flow>,
    version="<random version>",
    tags=["random tag"],
    schedule=null
)
```

Now that all the workflows are defined, we can now schedule automatics runs for these pipelines. \
Let's assume that we have a process that tells us that our model need to be retrained weekly based on 
some performance analysis. We also receive data to predict each hour.

Use prefect deployment object in order to : 
- Schedule complete ml process to run weekly
- Schedule prediction pipeline to run each hour

### More concepts with orchestration & prefect





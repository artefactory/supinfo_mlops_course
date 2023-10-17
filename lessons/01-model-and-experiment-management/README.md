## Module Program

### Experiment tracking intro

Experiment tracking is a crucial part of the machine learning lifecycle.
It involves logging and monitoring the experiments in a systematic way.
This allows for easy comparison of different runs, and helps in selecting the best model.

### What is MLflow

MLflow is an open-source platform that manages the end-to-end machine learning lifecycle.
It includes capabilities for experiment tracking, packaging code into reproducible runs, sharing and deploying models, and more.

### Experiment tracking with MLflow
MLflow Tracking is a component of MLflow that allows you to log and query experiments.
It logs parameters, code versions, metrics, and output files when running your machine learning code and allows for visualizing and comparing runs in its UI.

You can log metrics, parameters, artifacts (files), and models from your machine learning code in Python (what we will do today) or using REST / R / Java APIs.

MLflow Tracking includes a UI that lets you compare and contrast runs, evaluate metrics across experiments, and more.

As a ML Engineer, you will have to handle the following MlFlow concepts:
- Experiment: A run of a data science workflow. It can be a single training run or a series of runs.
- Run: A single execution of a workflow step in an experiment. E.g. on model training. A run will have a unique ID and can be associated with a user, a source code version, and other metadata.

You can associate your model parameters, evaluation results and model file with a run ID, and link this run ID to a specific experiment.

### Saving and loading models with MLflow
MLflow Models is another component that allows you to manage models.
It provides a standard format for packaging machine learning models that can be used in a variety of downstream tools.
It also provides utilities to save/load models and to create a serving stack for the model.

### Model registry
MLflow Model Registry is a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of an MLflow Model.
It provides model lineage, model versioning, stage transitions, and annotations.

### Practice
Now that you have a basic understanding of MLflow and its components, it's time to practice.
Try to implement a simple machine learning model and use MLflow to track its experiments, save the model, and register it in the Model Registry.

You'll have to navigate through [MLFlow Documentation](https://mlflow.org/docs/latest).

### Homework

Please go through the notebook associated with this lesson.

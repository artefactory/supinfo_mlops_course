# Model Deployment

## Intro

In this module we'll learn how to:

- Deploy a model
- Create a REST API that will serve our model predictions
- Dockerize the API
- Use locust to run some load tests

Model deployment is the process of making a machine learning (ML) model accessible to users. It involves creating an interface with which a user can interact with the model we developed. This interface accepts requests from users and sends back responses, so that they can be used in real-world applications.

> There are three different types of deployment:
- **Batch (offline)** : recurrent jobs that get automatically executed
- **Web Service (online)** : a server that awaits requests from clients and send back responses
- **Streaming (online)** : a consumer that awaits events from producers and triggers workflows

In this module, we will create a `web service` that can predict the *trip duration* for the NYC Taxi given the *pickup location ID*, *the drop off location ID* and the *number of passengers*.

## 4.2 - Model Deployment

We will use the REST architecture we covered in the theoretical part of the course to build our web service. There are several options of frameworks that allow us to package our model into a web service:

- FastAPI
- Flask
- Django

For this module, we will use FastAPI, a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

## Introduction to FastAPI

If you have never used FastAPI before, please refer to the [tutorial](./fast_api_tutorial/fast_api_tutorial.md) to have an introduction to the framework.

## Model Deployment Lab

### Goal of this Lab

### Exercises

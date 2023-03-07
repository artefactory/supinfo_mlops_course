# Overview
- 


## The goal of this lesson

In this lesson we will 
- first create a FastAPI application that will serve our model for inference. 
- We'll then containerize it this app and deploy as a local endpoint. 
- Finally we'll create simulate some load tests using `locust` to see how our model performs.

## Setup

## Create a virtual environment

```bash
conda create -n env_model_deployment python=3.9 -y
```

then activate it

```bash
conda activate env_model_deployment
```

### Install



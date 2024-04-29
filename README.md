## Overview

### Objective

Teach practical aspects of productionizing ML services — from collecting requirements to model deployment and monitoring.

### Target audience

Data scientists and ML engineers. Also software engineers and data engineers interested in learning about putting ML in production.

### Pre-requisites
For the best experience, we recommend that you have Docker, bash and Make installed on your machine. Follow the instructions to install them if you don't have them already.

* Python
* Docker
* Being comfortable with command line
* Prior exposure to machine learning
* Prior programming experience (at least 1+ year)

##  How to set up

### Installing prerequisites
Let's first make sure you have access to the Docker. If you are not sure, follow the instructions below.

#### Docker
Check that you have Docker desktop installed in your machine by running:

```bash
docker -v
```

If that is not the case, just follow the official instructions:

* [Install Docker - Mac OS](https://docs.docker.com/desktop/install/mac-install/)
* [Install Docker - Linux](https://docs.docker.com/desktop/install/linux-install/)
* [Install Docker - Windows](https://docs.docker.com/desktop/install/windows-install/)

For those of you working on Windows, you might need to update Windows Subsystem for Linux. To do so, simply open PowerShell and run:

```bash
wsl --update
```

Once docker is installed, make sure that it is running correctly by running:

```bash
docker run -p 80:80 docker/getting-started
```

If you check the Docker App, you should see a getting started container running. Once you've checked that this works correctly, remove the container via the UI.

<details>
    <summary><b>Optional</b></summary>
    You can also perform these operations directly from the command line, by running <code>docker ps</code> to check the running containers and <code>docker rm -f [CONTAINER-ID]</code> to remove it.
</details>

#### Bash
Check that you have bash installed in your machine by opening a terminal and running:

```bash
bash --version
```
This should be the case for all Mac and Linux users.

If you are using Windows, you can use the Git Bash terminal that comes with Git. You can download it [here](https://git-scm.com/downloads).

#### Make
Check that you have make installed in your machine by opening a terminal and running:

```bash
make -v
```
This should be the case for all Mac and Linux users.

If you are using Windows, you can then install make using Chocolatey. You can download Chocolatey [here](https://chocolatey.org/install).

Then, restart Git Bash and run:

```bash
choco install make
```

Restart Git Bash again and check that make is installed by running:

```bash
make -v
```

If you did not manage to install make, you can still follow the course by following the instructions in the next section under the label "Without `make` and `bash` installed on your terminal".

### Prepare the course infrastructure

Now, we will guide you to build the required Docker Images. With a terminal, go to the root of this folder.

First check that you have `make` installed by running `make -v`

<details>
    <summary><b>If you have `make` and `bash` installed on your terminal</b></summary>
    Then simply run:
    <p><pre>make prepare-mlops-crashcourse</pre></p>
</details>

<details>
    <summary><b>Without `make` and `bash` installed on your terminal</b></summary>
    Please run:
    <p><pre>docker build -t mlops_notebooks ./lesson/
docker build -t mlops_mlflow ./mlflow_server/</pre></p>
</details>

### Launch the course

Follow these steps to mount the two containers and open the user interface to start the course.

<details>
    <summary><b>If you have `make` and `bash` installed on your terminal</b></summary>
    You can directly bundle all this section's commands by typing:
    <p><pre>make launch-mlops-crashcourse</pre></p>
</details>

<details>
    <summary><b>Without `make` and `bash` installed on your terminal</b></summary>
    First, create a network:
    <p><pre>docker network create --driver bridge mlops-crashcourse</pre></p>
    <p>Then:</p>
    <p><pre>docker run -it --rm --user root -p 10000:8888 -p 8000:8000 -p 4200:4200 -v ${PWD}/mlflow_server/local:/mlflow -e JUPYTER_ENABLE_LAB=yes -e JUPYTER_TOKEN=docker -e MLFLOW_TRACKING_URI=http://mlflow:5001 --network mlops-crashcourse --name jupyter -d mlops_notebooks</pre></p>
    <p>And:</p>
    <p><pre>docker run -it -d --rm -p 5001:5000 -v ${PWD}/mlflow_server/local:/mlflow --network mlops-crashcourse --name mlflow mlops_mlflow</pre></p>
    <p>You can then open your favorite browser and open in two tabs the two urls we will be working with:</p>
    <ul>
    <li>http://localhost:10000</li>
    <li>http://localhost:5001</li>
    <ul>
</details>

Once the Jupyter server is launched, you will need to use a token to attach your browser to it. The token you should use is `MLOPS`.

### Time to work

All the activities of this course can be found in the `notebooks` folder. If you are using docker, then you will be working on jupyter lab and the folder will be immediately visible from the root. If instead, you are running this course locally on your computer, then you can find the notebooks under `lessons/{lesson-name}/notebooks`.

### Cleanup

Once you are done with the course, you can follow these steps to clean your workspace.

> Careful! This will destroy all your work if you did not save it locally.

<details>
    <summary><b>If you have `make` and `bash` installed on your terminal</b></summary>

    Then simply run:
    ```bash
    make clean-mlops-crashcourse
    ```
</details>

<details>
    <summary><b>Without `make` and `bash` installed on your terminal</b></summary>
    Please run

    ```bash
	docker stop jupyter
	docker stop mlflow
	docker image rm mlops_notebooks
	docker image rm mlops_mlflow
    docker network rm mlops-crashcourse
    ```
</details>

## Syllabus

### [Module 1: Introduction](lessons/01-intro)

* What is MLOps
* Why do we need MLOps
* Running example: NY Taxi trips dataset
* Course overview
* Environment preparation
* Practice
* Homework


### [Module 2: Pipeline and Orchestration](lessons/02-pipeline-and-orchestration)

* Introduction to workflows orchestration
* Introduction to Prefect
* From notebooks to workflows
* Continuous Training
* Next steps and resources
* Practice
* Homework


### [Module 3: Data Management](lessons/03-data-management)

* Testing Data Quality
* Creating Data Pipelines
* Feature Stores
* Data Leakage
* Training / Serving Skew
* Practice
* Homework


### [Module 4: Model and Experiment Management](lessons/04-model-and-experiment-management)

* Experiment tracking intro
* What is MLflow
* Experiment tracking with MLflow
* Saving and loading models with MLflow
* Model registry
* Practice
* Homework


### [Module 5: Model Deployment](lessons/05-model-deployment)

* Web service: model deployment with FastAPI
* Docker: containerizing a web service
* MLflow: retrieving a model from the model registry
* Locust: load testing a web service


### [Module 6: Practice](lessons/06-practice)

* End-to-end project with all the things above

## Instructors

- El Hamri Amale
- Guidi Ariel
- Quinquet Guillaume
- Si Larbi Karim
- Deschamps Mael

> If you encounter difficulties during, don't hesitate to call us for help

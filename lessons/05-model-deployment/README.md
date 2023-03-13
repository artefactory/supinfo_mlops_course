# Model Deployment

## Intro

In this module we'll learn how to deploy a model in production. We'll learn how to create a REST API that will serve our model predictions. We'll also learn how to dockerize the API. Finally we'll learn how to use locust to run some load tests.


## Model Deployment lab

### Goal of the lab
We want to have a REST API running that can predict *trip duration* for the NYC Taxi given the *pickup locatoin ID*, *the dropoff location ID* and the *number of passengers*.


### Lab
Once the infra is running (`make prepare-mlops-crashcourse` and `make launch-mlops-crashcourse`)
1. Go inside jupyter container (starting in `/app` directory)
    - either by using VSCODE's `Remote Explorer` entension and  `attaching to running container`
    - or simply by going to the jupyter lab on `http://localhost:10000` on your browser
2. Go to `lessons/05-model-deployment`:
    ```bash
    cd lessons/05-model-deployment/
    ```
3. Initialize the course:
    ```bash
    make init_course_model_deployment
    ```
    <details open>
    <summary>Details on the init</summary>
    <br>
    The init will do the following:
    <ul> 
        <li> install the dependencies for this lesson 
        <li> pull the data from internet 
        <li> build a local model that is saved in `web_service/local_models/`
        <li> copy this model to the shared volume 
        <li> push a model to the running MLFlow server and register it as production
    </ul>
    <br>
    </details>

4. Go to the `web_service` directory where there will be a local model already pushed to `web_service/local_models/`
    ```bash
    cd web_service
    ```
5. You can run the api locally by running the following command:
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    Doing so you'll have the api running on `http://localhost:8000` sice this port is forwarded to the host's port 8000 you can interact with the api from your host machine.

    1. You can go to `http://localhost:8000/docs` to see the documentation of the api (where you can also test the api)

    2. You can also use `curl` to test the api's health : `curl http://localhost:8000`

    3. You can send requests to the running api using python (example inside container openning another terminal):
        ```bash
        cd /app/lessons/05-model-deployment/ &&
        python bin/post_payload.py
        ```

    4. You can also send a request to the api using `curl`:
        ```bash
        curl -X POST 'http://localhost:8000/predict'\
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
          "PULocationID": 264,
          "DOLocationID": 264,
          "passenger_count": 2}'
        ```
        - (optionnal) create payload file creating a file `test_payload.json` with the following content:
        ```json
        {"PULocationID": 264,
         "DOLocationID": 264,
         "passenger_count": 2}
        ```

        - or using `cat`: 
        ```bash
        cat << EOF > test_payload.json
        {
        "PULocationID": 264,
        "DOLocationID": 264,
        "passenger_count": 2
        }
        EOF
        ```
        
        - then you can send request using the payload file:
        ```bash
        curl -X POST \
          'http://localhost:8000/predict' \
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d @test_payload.json
        ```
6. Now that you understood how to create an api locally, you can create a docker image for the api. Since we're working with code that is inside the running container, you you'll to run the following commands from the host machine (not inside the container):
    1. Build the docker image (you should be inside the `05-model-deployment` directory):
        - first you must move the model `pipeline__v0.0.1.joblib` that was copied to the shared volume during the init of the course from `infra/mlflow_server/local/` to `web_service/local_models/`:
            ```bash
            mv ../../infra/mlflow_server/local/pipeline__v0.0.1.joblib web_service/local_models/
            ```
        - then you can build the docker image:
            ```bash
            docker build -t prediction_server -f Dockerfile.app .
            ```
    2. Run the docker image:
        ```bash
        docker run -itd --rm --name prediction_server -p 8001:8001 --network mlops-crashcourse-supinfo prediction_server
        ```
    3. Check if the container is running:
        ```bash
        docker ps
        ```
    4. Check if the api is running:
        - go to `http://localhost:8001/docs` to see the documentation of the api (where you can also test the api)

    5. You can send requests to the running dockerized api using python (example inside container openning another terminal):
        - change the host in `/app/lessons/05-model-deployment/bin/post_payload.py` to `http://prediction_server:8001`

        - then just like previously you can run:
            ```bash
            cd /app/lessons/05-model-deployment/ &&
            python bin/post_payload.py
            ```

    6. you can stop the prediction server from the host machine:
        ```bash
        docker stop prediction_server
        ```
    7. you can remove the prediction server image from the host machine:
        ```bash
        docker image rm prediction_server
        ```

7. Once you're done with this simple version, your turn to build a more complex version of the api that pulls the model from the running MLFlow server.
    > **Note**: You can find the solution to this lab in the `solution.zip`.

8. Locust inside the jupyter container (you should be inside the `05-model-deployment` directory):
    1. Run locust:
        ```bash
        locust -f ./locust/locustfile.py --host=http://localhost:8000
        ```
    3. Go to `http://localhost:8089` to see the locust dashboard
    4. Start the swarm


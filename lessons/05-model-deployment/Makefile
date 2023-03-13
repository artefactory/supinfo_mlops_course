.DEFAULT_GOAL = help

.PHONY: init_course_model_deployment
init_course_model_deployment:
	@echo "Initializing the course model deployment lesson..."
	@apt-get install curl -y
	@python -m pip install -r requirements_dev.txt
	@echo "Getting the data..."
	@python ./bin/get_data.py
	@echo "Building local model..."
	@python ./bin/build_model.py
	@echo "Copiying local model to shared volume..."
	@cp web_service/local_models/pipeline__v0.0.1.joblib /mlflow
	@echo "Building model and pushing to Mlflow..."
	@python ./bin/build_model_mlflow.py
	@echo "Ready, you can now start."

.PHONY: help
help:
	@echo
	@echo "Welcome to the model deployment lesson!"
	@echo
	@echo "Available commands:"
	@echo
	@echo "make init_course_model_deployment"
	@echo "	- Prepare the course environment (get data, build local model in the web_service folder, \n\t  push model to running mlflow and register it as production stage)."
	@echo 
	@echo "make help"
	@echo "	- Show this help message."
	@echo

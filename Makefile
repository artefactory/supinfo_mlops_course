.DEFAULT_GOAL = help

prepare-mlops-crashcourse: welcome confirmation build-all ready

launch-mlops-crashcourse: create-network run-all open-ui

clean-mlops-crashcourse: stop-all remove-all remove-network clean-mlflow goodbye

#################
# 	 DOCKER	    #
#################

create-network:
	@echo "Creating the course docker network..."
	-@docker network create --driver bridge mlops-crashcourse-supinfo

remove-network:
	@echo "Removing the course docker network..."
	-@docker network rm mlops-crashcourse-supinfo

build-all: build-lesson build-mlflow

build-lesson:
	@echo "Building lesson jupyter lab container..."
	@docker build -t mlops_notebooks_supinfo -f infra/jupyter/Dockerfile .

build-mlflow:
	@echo "Building lesson mlflow container..."
	@docker build -t mlops_mlflow_supinfo ./infra/mlflow_server/

remove-all:
	@echo "Removing all course images..."
	-@docker image rm mlops_notebooks_supinfo
	-@docker image rm mlops_mlflow_supinfo

run-all: run-lesson run-mlflow

run-lesson:
	./infra/jupyter/bin/run_lab.sh

run-mlflow:
	./infra/mlflow_server/run_server.sh

stop-all:
	@echo "Stopping all course containers..."
	-@docker stop jupyter
	-@docker stop mlflow

clean-mlflow:
	@echo "Removing all mlflow data..."
	-@rm -rf ./infra/mlflow_server/local/artifacts
	-@rm -rf ./infra/mlflow_server/local/mlflow.db

#################
# 	 	CI	    #
#################

.PHONY: run-linter
run-linter:
	@echo "Running linter and code formatting checks"
	@isort . --check --diff --profile black
	@black --check .
	@flake8 .

.PHONY: install-precommit
install-precommit:
	@pre-commit install -t pre-commit

.PHONY: format-code
format-code:
	@pre-commit run --all-files

#################
# 	   MISC	    #
#################

.PHONY: welcome
welcome:
	@echo
	@echo "Welcome to the Artefact MLOps crash course!"
	@echo "This util will help you prepare the course dependencies and run them."
	@echo "You can run 'make help' to see the available commands."

.PHONY: confirmation
confirmation:
	@echo "We will now start the installation of course infrastructure."
	@echo "If this fails, make sure Docker is installed and running."
	@echo "This might take a few minutes depending on your computer and connexion."
	@echo "Are you ready? [y/N] " && read ans && [ $${ans:-N} = y ]

.PHONY: ready
ready:
	@echo
	@echo "The docker images for the mlflow server and the jupyter lab have now been created."
	@echo "Thank you for your patience!"
	@echo "You can now run the command 'make launch-mlops-crashcourse' in the console to launch the course."
	@echo

.PHONY: goodbye
goodbye:
	@echo
	@echo "Thanks for participating in the Artefact MLOps crash course!"
	@echo

.PHONY: open-ui
open-ui:
	@open http://localhost:5001
	@open http://localhost:10000

.PHONY: help
help:
	@echo
	@echo "Welcome to the Artefact MLOps crash course!"
	@echo "This util will help you prepare the course dependencies and run them."
	@echo
	@echo "Available commands:"
	@echo
	@echo "make prepare-mlops-crashcourse"
	@echo "	- Prepare the course environment by building the docker images."
	@echo
	@echo "make launch-mlops-crashcourse"
	@echo "	- Launch the course environment by running the docker containers."
	@echo
	@echo "make clean-mlops-crashcourse"
	@echo "	- Clean the course environment by removing the docker containers and images."
	@echo
	@echo "make run-linter"
	@echo "	- Run the linter and code formatting checks."
	@echo
	@echo "make install-precommit"
	@echo "	- Install the pre-commit hooks."
	@echo
	@echo "make format-code"
	@echo "	- Run the pre-commit hooks."
	@echo
	@echo "make help"
	@echo "	- Show this help message."
	@echo

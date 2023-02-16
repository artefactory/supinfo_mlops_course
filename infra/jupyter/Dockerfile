FROM jupyter/minimal-notebook

# Set working directory to /app
WORKDIR /app

# Copying and installing course requirements
COPY ./infra/jupyter/requirements.txt ./requirements.txt
COPY ./infra/jupyter/bin ./bin

USER root
RUN apt update
RUN apt install build-essential -y
USER jovyan

RUN bash ./bin/install_requirements.sh

# Copying lesson contents
COPY ./lessons/ ./lessons

RUN mkdir outputs

ENV PYTHONPATH "$PYTHONPATH:/app/lib"

# Expose port 8888 for jupyter lab
EXPOSE 8888
# Expose port 5000 for mlflow server
EXPOSE 5000
# Expose port 8000 for deployed model
EXPOSE 8000
# Expose port 4200 for prefect
EXPOSE 4200

# Run Jupyter Lab when container starts up
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--NotebookApp.token='MLOPS'"]

FROM jupyter/datascience-notebook

# Set working directory to /app
WORKDIR /app

# Copying and installing course requirements
COPY ./devops/lesson/requirements.txt ./requirements.txt
COPY ./devops/lesson/bin ./bin
RUN bash ./bin/install_requirements.sh

# Copying lesson contents
COPY ./notebooks/ ./notebooks

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

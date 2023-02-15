#!/bin/sh

SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
echo "SCRIPTPATH: $SCRIPTPATH"

docker run -it -d --rm -p 5001:5000 -v ${SCRIPTPATH}/local:/mlflow --network mlops-crashcourse-supinfo --name mlflow mlops_mlflow_supinfo

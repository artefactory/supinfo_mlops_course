import time
from prefect import task, flow
from prefect.task_runners import SequentialTaskRunner


###################################
# Open work : Think about concurrent
# flow for NYC taxi trip duration
# Prefect support Async function
###################################

@task
def print_values(values):
    for value in values:
        time.sleep(1)
        print(value)
        print(value, end="\r")


@flow
def concurrent_flow():
    print_values(["Task A"] * 15)
    print_values(["Task B"] * 10)


@flow(task_runner=SequentialTaskRunner())
def sequential_flow():
    print_values(["Task A"] * 15)
    print_values(["Task B"] * 10)


if __name__ == "__main__":
    concurrent_flow()
    # sequential_flow()

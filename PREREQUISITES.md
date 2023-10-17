# Prerequisites and Setup

> [!Important]
> The course is dense.
>
> You won't have time to install and configure everything on D-day.
>
> You won't be able to follow the course if you don't have everything installed and working.
>
> 📣 **Please make sure you have everything installed and working before the course starts.** 📣
>
> You know your school WiFi better than we do, don't gamble on it.

> [!Important]
> We will be using Docker for this course, which can use up a lot of your disk.
> Make sure to have at least 10Gb available in your disk before starting this course. Otherwise you risk running into some obscure errors.

> [!Note]
> Each section has a **Check your Installation** section.
> Please make sure you can run the commands in that section before moving on to the next section.


## How to debug

1. Check and try to understand your error message
2. Google it / StackOverflow it
3. If you can't find a solution, ask your friends
4. If your friends can't help you, ask us on Slack


<details>
  <summary>📚 Table of Contents</summary>

  - [Docker Desktop](#docker-desktop)
    - [Download and Install Docker Desktop](#download-and-install-docker-desktop)
    - [✅ Check your Installation](#✅-check-your-installation)
    - [Pull a Docker Image](#pull-a-docker-image)
    - [✅ Check that it works](#✅-check-that-it-works)
  - [Install Git](#install-git)
    - [Download & Install](#download-&-install)
    - [Configure Git](#configure-git)
    - [✅ Check your Installation](#✅-check-your-installation)
  - [Conda + Python](#install-conda-+-python)
    - [Conda or MiniConda](#conda-or-miniconda)
      - [Install Miniconda](#install-miniconda)
      - [✅ Check your Installation](#✅-check-your-installation)
    - [Conda Environment](#conda-environment)
      - [Create Conda Environment](#create-conda-environment)
      - [Activate Conda Environment](#activate-conda-environment)
      - [✅ Check your Installation](#✅-check-your-installation)
    - [Install requirements](#install-requirements)
      - [Create and install requirements](#create-and-install-requirements)
      - [✅ Check your Installation](#✅-check-your-installation)

</details>


## Docker Desktop

Docker Desktop is a tool for MacOS and Windows machines for the building and sharing of containerized applications and microservices. It includes Docker Engine, Docker CLI client, Docker Compose, Notary, Kubernetes, and Credential Helper. It also features an intuitive user interface that makes managing your Docker images and containers locally much easier.

### Download and Install Docker Desktop

> [!Warning]
> 📣 **This step is the most time consuming one. You will not be able to perform it at HEC.** 📣

If you do not have `Docker Desktop` installed, you will need to install it. You can follow the official instructions:

* [Install Docker - Mac OS](https://docs.docker.com/desktop/install/mac-install/)
* [Install Docker - Linux](https://docs.docker.com/desktop/install/linux-install/)
* [Install Docker - Windows](https://docs.docker.com/desktop/install/windows-install/)

For those of you working on Windows, you might need to update Windows Subsystem for Linux. To do so, simply open PowerShell and run:

```bash
wsl --update
```

### ✅ Check your Installation

Once docker is installed, make sure that it is running correctly by running:

```bash
$ docker run -p 80:80 docker/getting-started
```

If you check the Docker App, you should see a getting started container running. Once you've checked that this works correctly, remove the container via the UI.

<details>
    <summary><b>Optional</b></summary>
    You can also perform these operations directly from the command line, by running <code>docker ps</code> to check the running containers and <code>docker rm -f [CONTAINER-ID]</code> to remove it.
</details>

### Pull a Docker Image

During session 2 of this course, you will need to build a Docker image yourself. To speed up the building process, you can pre-build your image.

Place your terminal at the root of the project and run:

```bash
$ docker build -t "nyc-taxi:prerun" -f "lessons/02-model-deployment/app.Dockerfile" ./lessons/02-model-deployment
```

### ✅ Check that it works

You should be able to see your image in the Docker Desktop UI:

![Docker Image](./images/example_image.png)

You can also check that it worked that by running:

```bash
$ docker images
REPOSITORY   TAG        IMAGE ID       CREATED         SIZE
nyc-taxi     prerun     1878dadc8ab5   6 minutes ago   118MB
```

## Git

### Install Git

Git is a distributed version control system that allows multiple people to work on a project at the same time without overwriting each other's changes.
It's essential for any collaborative coding project.

#### Download & Install
To install Git, follow the instructions on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Choose the instructions that match your operating system.

After installation, you can verify that Git is correctly installed by opening a terminal and typing:

```bash
$ git --version
```

This should return the version of Git that you installed.

#### Configure Git

After installing Git, you need to configure it with your name and email address.
This is important because every Git commit uses this information, and it's immutably baked into the commits you start creating:

```bash
$ git config --global user.name "Your Name"
$ git config --global user.email "you email@foo.bar"
```

You can find full configuration instruction on the [official Git website](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup).

### [OPTIONAL] Windows only: `git bash`

If you are using Windows, you can use PowerShell as your terminal.
But Powershell is limited and doesn't support all the commands we will use in this course.
You will need to install [`git bash`](https://gitforwindows.org/) to have access to all the commands we will use in this course.

Please carefully follow [instructions here](https://github.com/git-for-windows/git/releases/tag/v2.42.0.windows.2).

> Note: you can also use WSL terminal, but it's a bit more complicated to use.

### ✅ Check your Installation

Open a terminal, you should be able to run the following commands:

```bash
$ git --version

```

```bash
$ git config --global --list
user.name=johndoe
user.email=johndoe@foo.bar
```

Try to reach pandas GitHub repo to check your connection to GitHub:
```bash
$ git ls-remote --get-url https://github.com/pandas-dev/pandas.git
https://github.com/pandas-dev/pandas.git
```

## Conda + Python

### Conda or MiniConda

[Conda](https://docs.conda.io/en/latest/) is a package manager that allows you to install and manage packages on your computer.
[Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a minimal installer for conda.
It includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others.


#### Install Miniconda

To install Miniconda, follow the instructions on the [official Miniconda website](https://docs.conda.io/en/latest/miniconda.html).


#### ✅ Check your Installation

Open a terminal, you should be able to run the following commands:

```bash
$ conda --version
conda 22.9.0
```

```bash
$ conda env list
base                     /path/to/miniconda3
```

### Conda Environment

#### Create Conda Environment

A conda environment is a directory that contains a specific collection of conda packages that you have installed.
For example, you may have one environment with NumPy 1.7 and its dependencies, and another environment with NumPy 1.6 for legacy testing.
Or one environment with Python 3.8 and dependencies for project A and another with Python 3.7 for project B.

To create a conda environment, run:

```bash
$ conda create --name mlops-course python=3.10 -y
```

#### Activate Conda Environment

To use python version and dependencies from a conda environment, you need to activate it.

To activate the environment, run:
```bash
$ conda activate mlops-course
```

> [!Warning]
> **for Windows users**, you might need to run `conda init powershell` before being able to activate the environment.
> Please see [conda documentation](https://conda.io/projects/conda/en/latest/dev-guide/deep-dives/activation.html)
> and [this stackoverflow thread](https://stackoverflow.com/questions/64149680/how-can-i-activate-a-conda-environment-from-powershell) for more information.
>
> You might encounter other errors -> please google them (stackoverflow preferred) first.


#### ✅ Check your Installation

Open a terminal, you should be able to run the following commands and have a similar (not necessarily identical) output:

```bash
$ conda env list
base                     /path/to/miniconda3
mlops-course          *  /path/to/miniconda3/envs/mlops-course
```

```bash
$ conda info

     active environment : mlops-crash-test
    active env location : /Users/jules.bertrand/miniconda3/envs/mlops-crash-test
            shell level : 2
       user config file : /Users/jules.bertrand/.condarc
 populated config files :
          conda version : 22.9.0
    conda-build version : not installed
         python version : 3.10.6.final.0
       virtual packages : __osx=10.16=0
                          __unix=0=0
                          __archspec=1=x86_64
       base environment : /Users/jules.bertrand/miniconda3  (writable)
      conda av data dir : /Users/jules.bertrand/miniconda3/etc/conda
  conda av metadata url : None
           channel URLs : https://repo.anaconda.com/pkgs/main/osx-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/osx-64
                          https://repo.anaconda.com/pkgs/r/noarch
          package cache : /Users/jules.bertrand/miniconda3/pkgs
                          /Users/jules.bertrand/.conda/pkgs
       envs directories : /Users/jules.bertrand/miniconda3/envs
                          /Users/jules.bertrand/.conda/envs
               platform : osx-64
             user-agent : conda/22.9.0 requests/2.31.0 CPython/3.10.6 Darwin/23.0.0 OSX/10.16
                UID:GID : 502:20
             netrc file : None
           offline mode : False
```

```bash
$ conda list
# packages in environment at /Users/jules.bertrand/miniconda3/envs/mlops-course:
#
# Name                    Version                   Build  Channel
bzip2                     1.0.8                h1de35cc_0
ca-certificates           2023.08.22           hecd8cb5_0
libffi                    3.4.4                hecd8cb5_0
ncurses                   6.4                  hcec6c5f_0
openssl                   3.0.11               hca72f7f_2
pip                       23.3            py310hecd8cb5_0
python                    3.10.13              h5ee71fb_0
readline                  8.2                  hca72f7f_0
setuptools                68.0.0          py310hecd8cb5_0
sqlite                    3.41.2               h6c40b1e_0
tk                        8.6.12               h5d9f67b_0
tzdata                    2023c                h04d1e81_0
wheel                     0.41.2          py310hecd8cb5_0
xz                        5.4.2                h6c40b1e_0
zlib                      1.2.13               h4dc903c_0
```

```bash
$ python --version
Python 3.10.6
```

### Install requirements


#### Create and install requirements

> [!Warning]
> You will not have access to the course content before the course starts.
> So here is a requirements sample you should try to install before the course starts.

1. Create a `requirements-temp.txt` file
```bash
echo "scikit-learn==1.0.2
pandas==1.5.3
uvicorn==0.20.0
gunicorn==20.1.0
fastapi==0.88.0
mlflow==1.20.2" >> requirements-temp.txt
```

2. Install the requirements
```bash
pip install -r requirements.txt
```

#### ✅ Check your Installation

3. Check your requirements can be found in conda env
```bash
$ conda list fastapi
# packages in environment at /Users/jules.bertrand/miniconda3/envs/mlops-crash-test:
#
# Name                    Version                   Build  Channel
fastapi                   0.103.2                  pypi_0    pypi
```

4. Check you can access them from python
```bash
$ python
Python 3.10.13 (main, Sep 11 2023, 08:39:02) [Clang 14.0.6 ] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import fastapi
>>> fastapi.__version__
'0.88.0'
```

Thank you ✨ !

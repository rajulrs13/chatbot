# Simple ChatBot

> Server Side is built on python ( Flask )

## Description of Files
* **server.py** receives commands and queries and sends back message to the client.
* **chatbot_train.py** file trains the chatbot on the data available in the training_data folder. Once it is trained, the result will be stored as **db.sqlite** file.
* **chatbot.py** uses this **db.sqlite** file to generate responses for user queries.

## Get Started

- Creating a virtual environment ( optional )

``` bash
# install miniconda
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source .bashrc

# create a virtual environment and activate it
conda create --name <environment-name> python=3.7
source activate <environment-name>

```

- Installing the important python packages
``` bash
# install chatterbot
pip install chatterbot

# install flask
pip install flask

# install gunicorn
pip install gunicorn

```

- Running the server
``` bash
# running the server
gunicorn --bind 0.0.0.0:8000 server:app -t 300

```
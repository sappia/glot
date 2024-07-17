## Overview
A project covering various NLP applications using [langchain] (https://python.langchain.com/docs/get_started/introduction) framework and other ways of doing it.

## Translation
Translation is currently done in two ways. Each way has a separate endpoint. One way uses the [translators package](https://pypi.org/project/translators/) to translate given input text to the target language using the desired translator service (eg: google). The second way uses a local llm, eg: [llama3](https://ollama.com/library/llama3) to translate the given input text to the target language.

## Summarization
Summarization is done using a local llm, eg: [llama3](https://ollama.com/library/llama3) to summarize the given input text.

## Running the application using Docker
#### Setup
* Install the [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit)
* Add ollama service in addition to the uvicorn web server to docker compose file.
* Add the ollama-pull service to compose file to pull the model for the ollama container.
* Set environment variables for `OLLAMA_BASE_URL` and `LLM` in a `.env` file.
* See `compose.yaml` file for more information.


#### Build and run your application using docker
```shell
docker compose up --build
```
#### Stop your application using
```shell
CTRL+C
```
#### Stop and remove docker container using
```shell
docker compose down
```

#### On application startup
* Web server (Uvicorn) runs on ```http://0.0.0.0:8000```
* Ollama (your chosen local LLM) runs on ```http://0.0.0.0:11434```
* API Docs are accessible at ```http://127.0.0.1:8000/docs```

#### Tests
Tests can be run using pytest command inside the web docker container. The docker container can be accessed using ```docker exec -it <<container_name>> bash```

## Running the app locally
#### Setup
* Virtual environment
```
# Create virtual environment:
python3 -m venv env
# Activate env:
source env/bin/activate
```
* Installation
```
# Upgrade pip:
pip install --upgrade pip
# Install requirements:
pip install -r requirements.txt
```

* Download local LLM
```
# Download ollama:
curl -fsSL https://ollama.com/install.sh | sh
# Check local llm of choice (eg: llama3) runs using
ollama run llama3
```

#### Running the app
Run the fastapi app using
```uvicorn main:app --reload```

#### API Docs
Access the API docs to see the available endpoints at
```http://127.0.0.1:8000/docs```

#### Tests
Tests can be run using `pytest` command.

## Endpoints
* Available endpoints can be seen and requests to endpoints can be made from ```http://127.0.0.1:8000/docs```

OR

* By running a `curl` command like below:
```shell
curl -X 'POST' 'http://0.0.0.0:8000/translate_llm' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{
  "input_text": "Hello",
  "from_lang": "english",
  "to_lang": "french"
}'
```
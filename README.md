# Overview
A project covering various NLP applications using [langchain] (https://python.langchain.com/docs/get_started/introduction) framework and other ways of doing it.

## Translation
Translation is currently done in two ways. Each way has a separate endpoint. One way uses the [translators package](https://pypi.org/project/translators/) to translate given input text to the target language using the desired translator service (eg: google). The second way uses a local llm, eg: [llama3](https://ollama.com/library/llama3) to translate the given input text to the target language.

## Summarization
Summarization is done using a local llm, eg: [llama3](https://ollama.com/library/llama3) to summarize the given input text.

## setup
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
# Run the local llm of choice using
ollama run llama3
```

## Running the app
Run the fastapi app using
```uvicorn main:app --reload```

## API Docs
Access the API docs to see the available endpoints at
```http://127.0.0.1:8000/docs```
## glot overview
A project covering various NLP applications.

## translate
The translate endpoint uses the [translators package](https://pypi.org/project/translators/) to translate given input text to the target language using the desired translator service (eg: google).

## translate_llm
The transalte_llm endpoint uses a local llm (eg: llama3) to translate the given input text to the target language.

## setup
### Create virtual environment:
```python3 -m venv env```

### Activate env:
```source env/bin/activate```

### Upgrade pip:
```pip install --upgrade pip```

### Install requirements:
```pip install -r requirements.txt```

### Download ollama:
```curl -fsSL https://ollama.com/install.sh | sh```

## Run the local llm using
```ollama run llama3```

## Run the app using
```uvicorn main:app --reload```

## Access the API docs at
```http://127.0.0.1:8000/docs```
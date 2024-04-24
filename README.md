## glot overview
A project covering various NLP applications.

## translate
The translate endpoint uses the [translators package](https://pypi.org/project/translators/) to translate given input text to the target language using the desired translator service (eg: google).

## setup
Create virtual environment:
`python3 -m venv env`
Activate env:
`source env/bin/activate`
Upgrade pip:
`pip install --upgrade pip`
Install requirements:
`pip install -r requirements.txt`

## Run the app using
```uvicorn main:app --reload```

## Access the API docs at
```http://127.0.0.1:8000/docs```
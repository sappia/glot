from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_translate():
    response = client.post(
        "/translate",
        headers={"Content-Type": "application/json"},
        json={
            "input_text": "It is sunny today.",
            "from_lang": "en",
            "to_lang": "fr",
            "translator": "google"
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        "output": "Il fait beau aujourd'hui."
    }

def test_translate_unsupported_language():
    response = client.post(
        "/translate",
        headers={"Content-Type": "application/json"},
        json={
            "input_text": "It is sunny today.",
            "from_lang": "en",
            "to_lang": "fra",
            "translator": "google"
            },
    )
    assert response.status_code == 422
    assert response.text == '{"detail":"Failed to translate"}'

def test_translate_llm():
    response = client.post(
        "/translate_llm",
        headers={"Content-Type": "application/json"},
        json={
            "input_text": "Hello",
            "from_lang": "English",
            "to_lang": "French"
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        "output": "Bonjour"
    }


def test_summarize_llm():
    response = client.post(
        "/summarize_llm",
        headers={"Content-Type": "application/json"},
        json={
            "input_text": "I would like to eat something delicious."
            },
    )
    assert response.status_code == 200
    # summary may not be the same each time
    # assert response.json() == {
    #     "output": "The speaker wants to enjoy a tasty meal."
    # }
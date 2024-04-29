from fastapi.testclient import TestClient

from main import app

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
            "input_text": "It is sunny today.",
            "from_lang": "English",
            "to_lang": "French"
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        "output": "Il fait soleil aujourd'hui."
    }
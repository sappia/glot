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


def test_summarize_llm():
    response = client.post(
        "/summarize_llm",
        headers={"Content-Type": "application/json"},
        json={
            "input_text": "Generative artificial intelligence (generative AI, GenAI, or GAI) is artificial intelligence capable of generating text, images, videos, or other data using generative models, often in response to prompts. Generative AI models learn the patterns and structure of their input training data and then generate new data that has similar characteristics. Improvements in transformer-based deep neural networks, particularly large language models (LLMs), enabled an AI boom of generative AI systems in the early 2020s. These include chatbots such as ChatGPT, Copilot, Gemini and LLaMA, text-to-image artificial intelligence image generation systems such as Stable Diffusion, Midjourney and DALL-E, and text-to-video AI generators such as Sora. Companies such as OpenAI, Anthropic, Microsoft, Google, and Baidu as well as numerous smaller firms have developed generative AI models. Generative AI has uses across a wide range of industries, including software development, healthcare, finance, entertainment, customer service, sales and marketing, art, writing, fashion, and product design. However, concerns have been raised about the potential misuse of generative AI such as cybercrime, the use of fake news or deepfakes to deceive or manipulate people, and the mass replacement of human jobs."
            },
    )
    assert response.status_code == 200
    assert response.json() == {
        "output": "Here is a concise summary:\n\nGenerative artificial intelligence (GAI) can create text, images, videos, or data using patterns learned from training data. GAI models have improved significantly with transformer-based deep neural networks, leading to the development of chatbots, image generators, and video generators by companies like OpenAI, Microsoft, and Google. While GAI has many applications across industries, concerns exist about its potential misuse in areas such as cybercrime, fake news, and job replacement."
    }
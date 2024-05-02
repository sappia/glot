from fastapi import FastAPI
from app.routers import api

tags_metadata = [
    {
        "name": "translate",
        "description": "The translate endpoint uses the translators package to translate given input text to the target language using the desired translator service (eg: google).",
    },
    {
        "name": "translate_llm",
        "description": "The transalte_llm endpoint uses a local llm, eg: llama3 to translate the given input text to the target language.",
    },
    {
        "name": "summarize_llm",
        "description": "The summarize_llm endpoint uses a local llm, eg: llama3 to summarize the given input text.",
    },
]

app = FastAPI(
    title="GlotAPI",
    description="Glot API provides endpoints for various NLP applications like translation, summarization etc.",
    openapi_tags=tags_metadata
)


app.include_router(api.router)
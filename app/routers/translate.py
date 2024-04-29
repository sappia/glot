import logging
import translators as ts

from fastapi import APIRouter, HTTPException
from app.schemas.translate import TranslatePayload, TranslateLLMPayload
from app.services.translate_llm import translate_llama3

router = APIRouter()

@router.post("/translate", tags=["translate"])
def translate(data: TranslatePayload):
    input_text = data.input_text
    from_lang = data.from_lang
    to_lang = data.to_lang
    translator = data.translator

    try:
        output = ts.translate_text(input_text, from_language=from_lang, to_language=to_lang, translator=translator)
    except Exception as e:
        logging.error(f"Failed to translate: {e}")
        raise HTTPException(status_code=422, detail=f"Failed to translate")

    return {"output": output}


@router.post("/translate_llm", tags=["translate_llm"])
def translate_llm(data: TranslateLLMPayload):
    input_text = data.input_text
    from_lang = data.from_lang
    to_lang = data.to_lang

    try:
        output = translate_llama3(from_lang, to_lang, input_text)
    except Exception as e:
        logging.error(f"Failed to translate: {e}")
        raise HTTPException(status_code=422, detail=f"Failed to translate")

    return {"output": output}
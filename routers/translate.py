import logging
import translators as ts

from fastapi import APIRouter
from schemas.translate import TranslatePayload

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
        output = f"Failed to translate: {e}"

    return {"output": output}


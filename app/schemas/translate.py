from pydantic import BaseModel


class TranslatePayload(BaseModel):
    input_text: str
    from_lang: str
    to_lang: str
    translator: str = 'google'


class TranslateLLMPayload(BaseModel):
    input_text: str
    from_lang: str
    to_lang: str
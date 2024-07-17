import os

from langchain_community.llms import Ollama
from langchain_core.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv(".env")
ollama_base_url = os.getenv("OLLAMA_BASE_URL")
llm_name = os.getenv("LLM")

def translate_llama3(from_lang, to_lang, input_text):
    llm = Ollama(temperature=0.0, model=llm_name, base_url=ollama_base_url)

    template = "Use good translator to translate from {input_language} to {output_language}. Give only translation without extra explanation."
    human_template = "{text}"

    chat_prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", human_template),
    ])

    prompt = chat_prompt.format_messages(input_language=from_lang, output_language=to_lang, text=input_text)

    output = llm.invoke(prompt)

    return output
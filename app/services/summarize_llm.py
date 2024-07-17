import os

from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from dotenv import load_dotenv


load_dotenv(".env")
ollama_base_url = os.getenv("OLLAMA_BASE_URL")
llm_name = os.getenv("LLM")

def summarize_llama3(input_text):
    # Split text
    text_splitter = CharacterTextSplitter()
    text = text_splitter.split_text(input_text)
    # Create multiple documents
    docs = [Document(page_content=t) for t in text]

    # Run Ollama
    llm = Ollama(temperature=0.0, model=llm_name, base_url=ollama_base_url)

    # Define prompt
    prompt_template = """Write a concise summary of the following:
    "{text}"
    CONCISE SUMMARY:"""
    prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

    # Define LLM chain
    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)

    summary = chain.run(docs)
    return summary
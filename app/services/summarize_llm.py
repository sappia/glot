from langchain.chains.summarize import load_summarize_chain
from langchain_community.llms import Ollama
from langchain_community.document_loaders import WebBaseLoader


def summarize_llama3(input_link):
    # load the doc to summarize
    loader = WebBaseLoader(input_link)
    docs = loader.load()

    # Run Ollama
    llm = Ollama(temperature=0.0, model="llama3")

    # Define LLM chain
    chain = load_summarize_chain(llm, chain_type="refine")

    summary = chain.run(docs)
    return summary
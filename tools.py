from langchain.tools import Tool
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

# Load environment variables (optional if you're using .env for other things)
load_dotenv()

def get_tools(llm):
    # Wikipedia Tool
    wiki_wrapper = WikipediaAPIWrapper()
    wiki_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

    # Load and embed your document
    loader = TextLoader("assets/data.txt", encoding='utf-8')  # Make sure this file exists and has Hindi content
    documents = loader.load()

    # ✅ Use LOCAL embedding model
    local_model_path = "models/paraphrase-multilingual-MiniLM-L12-v2"  # Downloaded manually
    embeddings = HuggingFaceEmbeddings(model_name=local_model_path)

    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Retrieval QA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return [
        Tool(
            name="Wikipedia Search",
            func=wiki_tool.run,
            description="Search historical facts or details from Wikipedia."
        ),
        Tool(
            name="DocumentQA",
            func=qa_chain.run,
            description="Useful for answering questions in Hindi from the provided document about a cricket match between new zealand and west indies."
        )
    ]

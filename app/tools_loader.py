from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.agents import Tool
from langchain.chains import RetrievalQA
import requests
from pydantic.v1 import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_community import GoogleSearchAPIWrapper


class DocumentInput(BaseModel):
    question: str = Field()

def get_online_pdf(url):
    """Function load online PDF url into PyPDFLoader"""
    response = requests.get(url, timeout=30)
    temp_file = './temp/file.pdf'
    # # write to new pdf
    with open(temp_file, 'wb') as f:
        f.write(response.content)
    # open and read
    loader = PyPDFLoader(temp_file)
    return loader

def get_prompt_template():
    """Function get prompt template for LLM Tool"""
    template = """
            If you don't know the answer, just say that you don't know.
            Don't try to make up an answer.
            {context}
            Give answers in point form.

            Question: {question}
            Answer:
            """
    return PromptTemplate(
        input_variables=["context", "question", "agent_scratchpad"], 
        template=template)

def create_llm_retrieval_qna_tool(prompt, llm, document_name, document_url):
    """Function creating RetrievalQA tool"""

    loader = get_online_pdf(document_url)
    pages = loader.load_and_split()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings()
    retriever = FAISS.from_documents(docs, embeddings).as_retriever()

    qna_tool = Tool(
            args_schema=DocumentInput,
            name= document_name,
            description=f"useful when you want to answer questions about {document_name}",
            func=RetrievalQA.from_chain_type(
                llm=llm,
                return_source_documents=True,
                retriever=retriever,
                chain_type_kwargs={
                    "prompt": prompt
                }
            )
        )
    
    return qna_tool


def load_tools(llm, default_document_url, updated_document_url):
    """Function loading Tools for LLM QnA and search engines"""

    tools = []
    # create tool for default document
    prompt_template = get_prompt_template()
    default_document_tool = create_llm_retrieval_qna_tool(
        prompt_template,
        llm,
        "DOCUMENT_DEFAULT",
        default_document_url)

    tools.append(default_document_tool)

    # create tool for updated document
    updated_document_tool = create_llm_retrieval_qna_tool(
        prompt_template,
        llm,
        "DOCUMENT_UPDATED",
        updated_document_url)

    tools.append(updated_document_tool)

    # creating google search tool
    search = GoogleSearchAPIWrapper()
    google_search_tool = Tool(
        name="GOOGLE_SEARCH",
        description="Search Google for recent results.",
        func=search.run,
    )
    tools.append(google_search_tool)

    # creating Tavily search tool
    tavily_search_tool = TavilySearchResults()
    tavily_search_tool.name = "TAVILY_SEARCH"
    tools.append(tavily_search_tool)

    return tools

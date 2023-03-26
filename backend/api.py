from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from fastapi import FastAPI
from langchain.llms import OpenAI
from dotenv import load_dotenv
from logging import getLogger
from fastapi.logger import logger
import logging

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers


load_dotenv()
app = FastAPI()

LLM = OpenAI(model_name="gpt-4", temperature=0.1, n=3, max_tokens=500)

RAG_TEMPLATE = """Based on the following federal regulation, answer the user’s prompt as an expert in OSHA compliance 
specializing in small business compliance.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
----------------
Regulation:
{legal_chunk}

User profile:
State: {state}
Business type: {business_type}
Number of employees: {num_employees}

chat_history:
{context}"""


@app.on_event("startup")
async def startup_event():
    """
    """

    logger.info("done initializing")

def generate_chat_response(query: str) -> str:

    system_template = """Use the following pieces of context to answer the users question. Based on the following federal regulation, answer the user’s prompt as an expert in OSHA compliance specializing in small business compliance.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    ----------------
    Regulation:
    {legal_chunk}

    User profile:
    State: {state}
    Business type: {business_type}
    Number of employees: {num_employees}

    chat_history:
    {context}"""

    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
    prompt = ChatPromptTemplate.from_messages(messages)

    user_profile = {
        "state": "CA",
        "business_type": "laundry",
        "num_employees": 150,
    }

    legal_chunk

    prompt_text = prompt.format(legal_chunk=legal_chunk, context=None, question=query, **user_profile)

    return LLM(prompt_text)


@app.post("/generate")
async def generate(query: str):
    return generate_chat_response(query=query)

if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)
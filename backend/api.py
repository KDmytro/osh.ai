# from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# from langchain.schema import (
#     AIMessage,
#     HumanMessage,
#     SystemMessage
# )

from fastapi import FastAPI
from langchain.llms import OpenAI
from dotenv import load_dotenv
from fastapi.logger import logger
import logging

from backend.doc_retrieval import legal_doc_selector
from backend.history_memory import ChatHistory
from backend.models import GenerateRequest, UserProfile

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers


load_dotenv()
app = FastAPI()

LLM = OpenAI(model_name="gpt-4", temperature=0.1, n=3, max_tokens=500)
chat_history = ChatHistory()


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



@app.on_event("startup")
async def startup_event():
    """
    """

    logger.info("done initializing")


def generate_chat_response(query: str, user_profile: UserProfile, topic: str) -> str:

    user_profile = {
        "state": user_profile.state,
        "business_type": user_profile.business_type,
        "num_employees": user_profile.num_employees,
    }

    legal_doc = legal_doc_selector.get(topic, {}).get("contents")

    history = chat_history.get_history()

    prompt_text = prompt.format(legal_chunk=legal_doc, context=history, question=query, **user_profile)

    answer = LLM(prompt_text)

    chat_history.add(question=query, answer=answer)

    return answer


@app.post("/generate")
async def generate(generate_request: GenerateRequest):
    query = generate_request.query
    user_profile = generate_request.user_profile
    topic = generate_request.topic

    return generate_chat_response(query=query, user_profile=user_profile, topic=topic)


@app.post("/clear_history")
async def clear_history():
    chat_history.clear()


if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)
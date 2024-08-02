import os
import os.path
from dotenv import find_dotenv, load_dotenv
from langchain.agents import (
    AgentExecutor,
    OpenAIFunctionsAgent,
    create_openai_functions_agent,
)
import openai
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage
from langchain.prompts import MessagesPlaceholder
from tools_loader import load_tools

load_dotenv(find_dotenv())

DEFAULT_DOCUMENT_URL = os.getenv("DEFAULT_DOCUMENT_URL")
UPDATED_DOCUMENT_URL = os.getenv("UPDATED_DOCUMENT_URL")
openai.api_key = os.getenv("OPENAI_API_KEY")
llm_model = os.getenv("OPENAI_MODEL")


def get_agent_prompt_template():
    """Function generate agent prompt template"""

    message = SystemMessage(
    content=(
            "You will be reading two documents and comparing the differences."
            "You will be using the previous conversation history if the user/human ask question on previous conversation. Make sure the human questions on responses explained in super simple terms in simple English"
        )
    )

    prompt = OpenAIFunctionsAgent.create_prompt(
        system_message=message,
        extra_prompt_messages=[MessagesPlaceholder(variable_name="chat_history")],
    )

    return prompt



def load_agent_executor():
    """Function loads the agent and the tools"""
    prompt_template_agent = get_agent_prompt_template()
    llm = ChatOpenAI(temperature=0.0, model=llm_model)

    # Loading tools.
    tools = load_tools(
        llm,
        default_document_url=DEFAULT_DOCUMENT_URL,
        updated_document_url=UPDATED_DOCUMENT_URL,
    )

    agent = create_openai_functions_agent(llm, tools, prompt_template_agent)

    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools,
        return_intermediate_steps=True,
        verbose=True
    )

    return agent_executor
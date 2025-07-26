# import os
# from dotenv import load_dotenv

# from langchain.agents import initialize_agent, AgentType
# from langchain.memory import ConversationBufferMemory
# from langchain_groq.chat_models import ChatGroq

# from character import get_professor_prompt
# from tools import get_tools

# # Load environment variables
# load_dotenv()
# assert os.getenv("GROQ_API_KEY"), "Please set GROQ_API_KEY in your .env"

# # Set up custom system prompt
# custom_prompt = get_professor_prompt()

# # Load tools


# # Load LLM from Groq
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.1,
#     max_tokens=512,
#     max_retries=2
# )

# tools = get_tools(llm)
# # Conversation memory
# memory = ConversationBufferMemory(
#     memory_key="chat_history",
#     return_messages=True,
#     input_key="input"
# )

# # Initialize the agent with memory and tools
# agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
#     verbose=True,
#     memory=memory,
#     agent_kwargs={
#          "prompt": custom_prompt
#     }
# )



# # Query function
# def ask_professor_neel(query: str) -> str:
#     return agent.run(query)

# def get_response(query: str) -> str:
#     return agent.run(query)
import os
from dotenv import load_dotenv

from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_groq.chat_models import ChatGroq

from character import get_professor_prompt
from tools import get_tools

# Load environment variables
load_dotenv()
assert os.getenv("GROQ_API_KEY"), "Please set GROQ_API_KEY in your .env"

def get_agent():
    # Set up custom system prompt
    custom_prompt = get_professor_prompt()

    # Load LLM from Groq
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.1,
        max_tokens=512,
        max_retries=2
    )

    tools = get_tools(llm)

    # Conversation memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        input_key="input"
    )

    # Initialize the agent with memory and tools
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        agent_kwargs={
            "prompt": custom_prompt
        }
    )
    return agent

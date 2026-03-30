
#Step1: Setup Api Keys for groq , openai and tavily
import os
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY=os.getenv("GROQ_API_KEY")

TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")

#OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")


#step2 setup LLM and tools 

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage


search_tool=TavilySearch(max_results=2)

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearch(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm,
        tools=tools
        
    )
    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful AI assistant."),
    HumanMessage(content="""
        LangChain is a Python framework for developing applications using large language models.
        Tell me more about LangChain and how it is used in AI development.
    """)
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)

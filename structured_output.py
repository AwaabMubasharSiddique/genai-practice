from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

class Review(TypedDict):
    summary: str
    sentiment:str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke('The hardware is great but the software feels bloated. There are too many preinstalled apps i cannot delete.UI looks outdated. Hoping for a software update to fix this')
print(result)
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from config import GROQ_API_KEY

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile"
)

search_tool = DuckDuckGoSearchRun()

def research(query: str):
    search_result = search_tool.run(query)
    
    messages = [
        HumanMessage(content=f"""
        Based on this search result, give a clear summary:
        
        Query: {query}
        Search Result: {search_result}
        """)
    ]
    
    response = llm.invoke(messages)
    return response.content

if __name__ == "__main__":
    print(research("What is artificial intelligence?"))
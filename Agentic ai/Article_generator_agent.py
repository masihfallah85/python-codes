#Article_generator_agent

"""
In this script we impeent an agent wich uses wikipedia,wolfram,arxiv data to form an article about a subject
"""

#Libraries
import os

from operator import itemgetter

from typing import Dict

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper, WolframAlphaAPIWrapper

#Loading api key
load_dotenv()

#Knowledge tools
wiki = WikipediaAPIWrapper(top_k_results = 1,doc_content_chars_max = 2000)

wolfram = WolframAlphaAPIWrapper()

arxiv = ArxivAPIWrapper(top_k_results = 1,doc_content_chars_max = 2000)

#Function for tools
def wikipedia_search(query : str) -> str:

    """This functions seach wikipedia"""

    try:

        return wiki.run(query)
    
    except Exception as e:

        return f"wikipedia error: {e}"
    

def wolfram_search(query : str) -> str:

    """This function searchs wolfram"""

    try:

        return wolfram.run(query)
    
    except Exception as e:

        return f"wolfram error: {e}"
    

def arxiv_search(query : str) -> str:

    """This function searchs arxiv"""

    try:

        return arxiv.run(query)
    
    except Exception as e:

        return f"arxiv error: {e}"
    

#Initialize model
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature = 0.3)


#Parallel research chain
research_chain = RunnableParallel(
    {
        "wiki_search_result": RunnableLambda(wikipedia_search),

        "wolfram_search_result" : RunnableLambda(wolfram_search),

        "arxiv_search_result" : RunnableLambda(arxiv_search),

        "topic" : RunnablePassthrough()
    }

)

#Prompt for article genrator
writer_prompt = ChatPromptTemplate.from_template(

    """
    You are an expert technical writer. You have gathered data from three sources on the topic: "{topic}".
    
    Here is the raw data:

    1. Wikipedia (General Context): {wiki_search_result}
    
    2. Wolfram Alpha (Hard Data/Math/Facts): {wolfram_search_result}
    
    3. Arxiv (Scientific/Academic Research):** {arxiv_search_result}
    
    ---
    TASK:
    Write a comprehensive, "augmented" article about {topic}. 

    - Synthesize the general context from Wikipedia with the hard math/science data from Wolfram and the cutting-edge research from Arxiv.

    - If sources conflict, note the discrepancy.

    - Cite your sources in the text (e.g., "According to Arxiv...").

    - Use Markdown formatting with headers.

    """
)

#Complete agent 
full_chain = research_chain | writer_prompt | model | StrOutputParser()

if __name__  == "__main__":

    topic = input("enter topic: ")

    try:

        result = full_chain.invoke(topic)

        print("Article -> ")

        print("=" * 30)

        print(result)

        print("=" * 30)

    except Exception as e:

        print(f"error : {e}")

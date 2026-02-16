#Web_page_content_analyser_agent

"""In this script we impelment an agent wich searchs web for alink then summerise it's contents and criticaly analyze them"""

#libraries
import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.document_loaders import WebBaseLoader

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

def  analyze_web_content(url : str) :


    """Analyze and sumerize a web page"""

    #Loading api
    load_dotenv()


    #Initializing model
    model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature = 0)

    #Web page loader
    loader = WebBaseLoader(url)

    try:

        docs = loader.load()

        raw_text = docs[0].page_content[:20000]

    except Exception as e:

        return f"error loading {url}"
    
    #Prompts
    summarize_prompt = ChatPromptTemplate.from_template(

        """Summerize contents of this web page concisley,focuse on main argumetns,factual claims,and conclusion.

        {content}
        
        """
    )

    verify_prompt = ChatPromptTemplate.from_template(

        """

         analyze this summary criticaly,logicaly,and using facts,use this methods
         
         1.source reliabiltiy check

         2.fact check

         3.critical thinking

         4.logical analysis

         tell your reasoning of why its correct and why its not

         {summary}

          """
    )


    #chains

    summary_agent = summarize_prompt | model | StrOutputParser()

    verify_agent = verify_prompt | model | StrOutputParser()


    #Results
    summary = summary_agent.invoke({"content" : raw_text})

    verify = verify_agent.invoke({"summary" : summary})

    return summary , verify

#Main 
if __name__ == "__main__":

     

     web_page = input("enter web page link: ")


     summary,analyze = analyze_web_content(web_page)


     print("summary:")

     print(summary)

     print("=" * 50)

     print("verification:")

     print(analyze)

     print("=" * 50)









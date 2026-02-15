#Debator_agent.py


"""This script contains adebator agent,two agents arguing for and againts a concept,and a thrid natural agent forming conclusion"""


#Needed libraries
import os 

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableParallel

#Loading api key
load_dotenv()

#initializing model
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature = 0.5)

#Creating prompts
pro_prompt = ChatPromptTemplate.from_template(

    """You are an expert philosopher,logician debator.

       no  matter how absurd it is,try your best to argue for the topic{topic}.

       use bullet point indexed clean argument for topic such as syllagism but not bound to just syllagism,in style of syllagism.
    
    """
)

con_prompt = ChatPromptTemplate.from_template(

    """You are an expert philosopher,logician debator.

       no  matter how absurd it is,try your best to argue againts the topic{topic}.

       use bullet point indexed clean argument for topic such as syllagism but not bound to just syllagism,in style of syllagism.
    
    """

)

judge_prompt = ChatPromptTemplate.from_template(


    """You are an expert logician

    think criticaly and judge without bias these  two arguments and form a conclsion,explain strength,weak points of eahc argument befor forming aconclusion.

    pro_argument:

    {pro_argument}

    con_argument:

    {con_argument}

    """
)


#Create a parralel pro,con argument chain
debate_chain = RunnableParallel(

    pro_argument =(pro_prompt | model | StrOutputParser()),

    con_argument = (con_prompt | model | StrOutputParser())
)

#Create judge chain
judge_chain = (

    {"con_argument" : lambda x : x["con_argument"] , "pro_argument" : lambda x : x["pro_argument"]} 

    |judge_prompt | model | StrOutputParser()
)

#Main debate function
def main_debate_function():

    topic = input("What topic do you want agents to debate? ")

    argument = debate_chain.invoke({"topic" : topic})

    print(f"for : { argument["pro_argument"]}")

    print(f"againts : {argument["con_argument"]}")

    conclusion = judge_chain.invoke(argument)

    print(f"conclusion : {conclusion}")


if __name__ == "__main__" :

    main_debate_function()
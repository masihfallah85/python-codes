#Math_problem_solver_agent.py

"""
In this script we implement a math problem solver agent.
"""

#Libraries
import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough
 
#Loading Api keys
load_dotenv()

    
#Prompts

undrestanding_prompt = ChatPromptTemplate.from_template(

    """

    You are an expert mathatician and logician,

    in George polya's math method,undrestanding is first step at solving math problem.

    your goal is to genrate deep_undrestanding of the problem  {problem}

    1.explain problem in simple terms

    2.explain what it wants

    3.highlight important information of the problem

    4.add extra helpfu linformatin if nececry

    your output should be bullet points eahc bullet point is one detail based on 1-4 processes.
"""
)

analyze_prompt = ChatPromptTemplate.from_template(

    """

    you are an expert mathmatician and logcian.


    this is problem {problem} this is your undrestanding of problem: {undrestanding}

    You should formulate an accurate plan for solving this problem base don undrestnading,but not actualy solving it

    your output should be an excat algorithm and steo bys eto excecution plan to solve problem

     """
)

synthesis_prompt = ChatPromptTemplate.from_template(


    """

    You are an expert mathatician and logician

    this is problem {problem} and your plan {plan}

    exacty exceute eahc plan carefully and accuretly.use tools if necessary

     output all excectuions you made.

  """

)

conclusion_prompt = ChatPromptTemplate.from_template(

    """

    You are an expert mathatican and logician

    this is problem {problem} and execution of it{execution}

    review eahc step carefully and add or remove things that you see nececry.

    output only and only the final solution of this problem,nothing else,not excecution steps etc...
   """
)

#Initialize model for undrestanding,synethesis and conclusion
model_1 = ChatGoogleGenerativeAI(model = "gemini-2.5-flash" , temperature = 0.1)

#Initialize model for analysis and plan making
model_2 = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature = 0.5)


#Creating chains
undrestanding_chain = undrestanding_prompt | model_1 | StrOutputParser()

analyze_chain = analyze_prompt | model_2 | StrOutputParser()

synthesis_chain = synthesis_prompt | model_1 | StrOutputParser()

conclusion_chain = conclusion_prompt | model_1 | StrOutputParser()

#Final agent
agent = (

    RunnablePassthrough.assign(undrestanding = undrestanding_chain) |

    RunnablePassthrough.assign(plan = analyze_chain) |

    RunnablePassthrough.assign(execution = synthesis_chain) |

    conclusion_chain
)

if __name__ == "__main__":

    problem = input("enter problem: ")

    result = agent.invoke({"problem" : problem})

    print(result)
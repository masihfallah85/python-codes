#Pc_task_agent


"""
In this task we implement an agent wich performs a task on pc using python
"""

#Libraries
import os

from typing import TypedDict, List

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.messages import HumanMessage, SystemMessage

from langchain_community.tools import DuckDuckGoSearchRun

from langchain_experimental.utilities import PythonREPL

#Loading api
load_dotenv()

#Tools
python_repl = PythonREPL()

search_tool  = DuckDuckGoSearchRun()


#Memmory state of agents
class agent_state(TypedDict):

    task : str

    plan_info : str

    search_results : str

    execution_output : str

    final_report : str


#Initialize model
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash",temperature = 0)

def planner_agent(state : agent_state):


    """Planner agent"""

    prompt = f"""
        You are a planner agent.

        You should suggest useful info about task : {state["task"]} related to pc  wich a seach agent searchs web,and give info to an excecuter aget wich executes it with ptyhon.

        your answer should be in bullet point format.
          """
    
    response = model.invoke([SystemMessage(content = "You are aplanner agent wich provide blue print for other agents"),HumanMessage(content=(prompt))])

    return {"plan_info": response.content}


def research_agent(state : agent_state):

    """Seach agent"""

    query = f"technical implemention details about task : {state["task"]} "

    search_result = search_tool.run(query)

    return {"search_results": str(search_result)}

def executor_agent(state: agent_state):

    """excecuter agent """

    prompt = f"""
    Based on these search results: {state["search_results"]}
    Write a Python script to perform the task: {state["task"]}
    
    RULES:
    1. You MUST use print() to output the final answer/data.
    2. ONLY output the raw python code. 
    3. No markdown backticks (```), no explanations.

    why this rules?so a python repl of langchain can excecute code properly
    """

    response = model.invoke(prompt)

    raw_resonse =  response.content

    code = raw_resonse.replace("```python", "").replace("```", "").strip()

    try:

        result = python_repl.run(code)

    except Exception as e:

        result = f"error during execution: {str(e)}"
        
    return {"execution_output": result}

def reporter_agent(state: agent_state):

    """final report agent"""

    prompt = f"""

    The task was: {state['task']}

    The useful info was {state['plan_info']}

    The technical execution result was: {state['execution_output']}
    
    Explain what happened to the user in simple, layman's terms. 

    Avoid technical jargon. If it failed, explain why simply.

    """
    report = model.invoke(prompt)

    return {"final_report": report.content}


def run_multimodal_agent(user_task: str):

    """Multi agent system"""

    state: agent_state = {"task": user_task, "plan_info": "", "search_results": "", "execution_output": "", "final_report": ""}
    
    state.update(planner_agent(state))

    state.update(research_agent(state))

    state.update(executor_agent(state))

    state.update(reporter_agent(state))
    
    print("=" * 30)

    print(state['final_report'])

    print("=" * 30)

if __name__ == "__main__":

    task = input("enter your task for pc: ")

    run_multimodal_agent(task)
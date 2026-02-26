#Router_coder_agent.py

"""
In this script we implement a coder agent using routing design pattern

"""

#Libraries
import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.messages import SystemMessage , HumanMessage

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnablePassthrough
#Loading api
load_dotenv()

#Initialzing model
model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash" , temperature = 0.3)

#Creating each possible route
def sorting_route(problem : str) -> str :

    """If problem can be solved by a sorting algorithm"""

    prompt = f"""

        This is problem {problem}

        we have conclued that it can be solved by a sorting algorithm.

        output the execution steps as bullet points each point idnicating one step using any sroting algorithm wich best fits the problem from insertion,selection,merge,heap,radix,count,bucket ...
        
        example:

        1.get input list of numbers from user

        2.use insertion sort on list to sort in descending order

        3.output newly sorted list 3rd index

        no other explnation,just output excecution steps

          """

    sort_chain =  model | StrOutputParser()

    result = sort_chain.invoke([SystemMessage(content= "You are an expert coder,algorithmic thinker"),HumanMessage(content= prompt)])

    return result


def hash_rout(problem : str) -> str :


    """If problem is solved by using a hash tabel"""


    prompt = f"""

     This is our problem {problem}

    we concluded that it can be solved by a hash tabel.

    output execution steps as bullet point wich each point is one step using hash tabel with hashing fucntion wich best fits the problem from open adressing,divison,universal ....

    example:

    1.get input from user

    2.identify this "any key from input" as key and put thm in a list

    3.use this "any hashing function you see fit"  we   place them in a hash table with colsion method and store them 

    4.go to that index of hash tabel

    5.output the answer

    output only bullet points,without firther explnation

    """

    hash_chain = model | StrOutputParser()


    result = hash_chain.invoke([SystemMessage(content= "You are an expert coder,algorithmic thinker"),HumanMessage(content= prompt)])

    return result


def graph_route(problem : str) -> str:

    """If problm is solvable by a graph algorithm"""


    Prompt = f"""

    This is our problem {problem}

     we concluded that it can be solved by a graph algorithm.

    output execution steps as bullet point wich each point is one step using any graph algorithm best fiting the problem like dfs,bfs,kruska ,prim, ..........

    example:

    1.get input from user

    2.form adacency list

    3.form prim algorithm this way "explain how to impelemnt the algorithm"

    4.form result of minimm spanning tree inadcaency list

    5.output the result

    output only bullet points,without firther explnation

        """
    

    graph_chain = model | StrOutputParser()

    result = graph_chain.invoke([SystemMessage(content = "you are an expert coder,algorithmic thinker"),HumanMessage(content= Prompt)])

    return result


def tree_route(problem : str) -> str:


    """If problem is solvabel by a tree algorithm"""


    prompt = f"""

    This is our problem {problem}


    we concluded that it can be solved by a tree.

    output execution steps as bullet point wich each point is one step of execution using a tree algorith wich best fitst the problem,from avl,binary searcht ree,heap tree,red blakc tree....

    example:

    1.get input from user

    2.form an avl tree ith adcency list "explain eahc step of forming avl"

    3.insert user inptus to avl this way

    4.find that node of avl with this codntions

    5.output the answer

    output only bullet points,without firther explnation

     """
    

    tree_chain = model | StrOutputParser()

    result = tree_chain.invoke([SystemMessage(content="you are an expert coder,algorithmic thinker"),HumanMessage(content=prompt)])

    return result

def stack_route(problem : str) -> str:

    """if problem is solved by using stack"""


    prompt = f"""
    
    This is our problem  {problem}

     we concluded that it can be solved by stack.

    output execution steps as bullet point wich each point is an execution stepp,using stack algorithms....

    example:

    1.get input from user

    2.create two stacks 

    3.insert inputs to these stacks this way

    4.if secodn stack si empty get top of other stack

    5.output the top

    output only bullet points,without firther explnation

      """
    
    stack_chain = model | StrOutputParser()

    result = stack_chain.invoke([SystemMessage(content= "you are an expert coder,algorithmic thinker"),HumanMessage(content= prompt)])

    return result

def queue_route(problem : str) -> str:


    """if problem is solved by queue"""


    prompt = f"""
       
      This is our problem {problem}

      we concluded that it can be solved by queue.

    output execution steps as bullet point wich each point is an excecution step,using queue....

    example:

    1.get input from user

    2.create a queue

    3.manipulate queue this way "explain how to manipulate"

    4.return front of queue  as answer

    output only bullet points,without firther explnation
    """

    queue_chain = model | StrOutputParser()

    result = queue_chain.invoke([SystemMessage(content = "You are an expert coder,algorithmic thinker"),HumanMessage(content = prompt)])


    return result

def deque_route(problem : str) -> str:

    """if problem is solvabel by deque"""

    prompt = f"""

    This is our problem {problem}

     we concluded that it can be solved by deque.

    output execution steps as bullet point wich each point is exectuion step using deque....

    example:

    1.get input from user

    2.create deque

    3.insert inputs to deque this way"explain how to insert"

    4.manipulate deque this way "explain how to manipulate deque"

    5.output front+back of deque 

    output only bullet points,without firther explnation
     """
    
    deque_chain = model | StrOutputParser()

    result = deque_chain.invoke([SystemMessage(content= "You are an expert coder,algorithmic thinker"),HumanMessage(content= prompt)])

    return result


def linked_list_route(problem : str) -> str:


    """If problem is solvabel by linked list"""


    prompt = f"""

    This is our problem {problem}

     we concluded that it can be solved by linked list.

    output execution steps as bullet point wich each point is one excecution step using linked llist ....

    example:

    1.get input from user

    2.create linked ist"explain how to create it"

    3.insert inputs in linked list "explain how to insert" 

    4.create two pointers,one fast pointer and one slow pointer with 2 and 1 steps

    5.find their closiion for node with is loop

    6.output the elemtn wich forms loop

    output only bullet points,without firther explnation

    """

    linked_list_chain = model | StrOutputParser()

    result = linked_list_chain.invoke([SystemMessage(content = "you are an expert coder,algorhtmic thinker"),HumanMessage(content=prompt)])

    return result

def optimization_route(problem : str) -> str:

    """If problem is solvabel by an optimization algorithm"""

    prompt = f"""

    This is our problem {problem}

     we concluded that it can be solved by an optimization algorithm.

    output execution steps as bullet point wich each point is one excecution step using an optmization algoorithm like combiantorical,linear....

    example:

    1.get input from user

    2.put them inside a list

    3.perform linear optimization this way"explain how"

    4.output the answer

    output only bullet points,without firther explnation

      """
    
    optimization_chain = model | StrOutputParser()

    result  = optimization_chain.invoke([SystemMessage(content = "you are an expert coder,algorithmic thinker"),HumanMessage(content = prompt)])

    return result


def formula_route(problem : str) -> str:

    """If problem is sovlabel by a formula"""


    prompt  = f"""

    This is our problem {problem}

     we concluded that it can be solved by a single forula.

    output execution steps as bullet point wich each point is one excecution step usinga formula like string amnipualtion,number theory,combinatronics ....

    example:

    1.get input from user

    2.use this number theoritc formula "explain which formula"

    3.output the answer

    only output the bulet points,wihtout any other addtional explnations

     """
    
    formula_chain = model | StrOutputParser()

    result = formula_chain.invoke([SystemMessage(content = "you are an expert coder,algorithmic thinker"),HumanMessage(content = prompt)])

    return result

def matrix_route(problem : str) -> str:

    """If problem is solvable by matrix"""


    prompt  = f"""

    This is our problem {problem}

     we concluded that it can be solved by matrix.

    output execution steps as bullet point wich each point is one excecution step using matrix....

    example:

    1.get input from user

    2.create matrix

    3.use this operation on matrix "explain what operations"

    4.output this entry of matrix

    only output the bulet points,wihtout any other addtional explnations

     """
    
    matrix_chain = model | StrOutputParser()

    result = matrix_chain.invoke([SystemMessage(content = "you are an expert coder,algorithmic thinker"),HumanMessage(content = prompt)])

    return result

#Decider function
def decider(input : str) -> str:

    """Decides wich route to take"""


    prompt = ChatPromptTemplate.from_template(

        """

        you are an expert coder,algorithmic thinker

       for this problem {input}

       decide wich one of this routes is the best solution,only output the route

       routes:

       -sort

       -hashtabel

       -graph

       -tree

       -stack

       -queue

       -deque

       -matrix

       -linkedlist

       -optimization

       -formula

       each route represents a class of algorithmic solutions

       examples of outputs for problems:

      output : linkedlist

      output : optimization

      output : formula

      exactly output name of route as exactly determined in this probpt,not anythingelse,as it ruins decison route,just one word.

      """
    )

    decider_chain = prompt | model | StrOutputParser()

    decision = decider_chain.invoke({"input" : input})


    if decision.lower() == "sort":

        result = sorting_route(input)

    elif decision.lower() == "hashtabel":

        result = hash_rout(input)


    elif decision.lower() == "graph":

        result = graph_route(input)

    elif decision.lower() == "tree":

        result = tree_route(input)

    elif decision.lower() == "stack":

        result = stack_route(input)

    elif decision.lower() == "queue":

        result = queue_route(input)


    elif decision.lower() == "deque":

        result = deque_route(input)

    elif decision.lower() == "matrix":

        result = matrix_route(input)

    elif decision.lower() == "linkedlist":

        result = linked_list_route(input)

    elif decision.lower() == "optimization":

        result = optimization_route(input)


    elif decision.lower() == "formula":

        result = formula_route(input)

    return result


#Coder agent 
prompt = ChatPromptTemplate.from_template(

    """

    you are an expert coder,algorithmic thinker

    this is our problem {problem}

    this is our exceution_steps {steps}

    write a python code wich is equvulant to exceution steps,only output python code

    example of output:

     python code:

     "your python code here"
   """
)

coder_chain = prompt | model | StrOutputParser()


#Final chain
final_chain = (

    RunnablePassthrough.assign(steps = lambda x : decider(x["problem"])) |

    coder_chain

)


if __name__ == "__main__":

    problem = input("enter your coding problem: ")


    result = final_chain.invoke({"problem" : problem})

    print(result)
    
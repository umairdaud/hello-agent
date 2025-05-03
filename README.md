# "Hello World" Agent using OpenAI Agent SDK using Google Gemini

This project demonstrate the steps required to create "Hello World" Ai Agent using OpenAi Agent SDK. Below are mentioned steps to create first Agent. 

# Step 1: Setup a Package using UV and Install necessary dependences 

First create a project with name "hello-agent" using uv command in CMD:

uv init --package hello-agent

After project is created go to hello-agent folder using command in CMD:

cd hello-agent

In the folder Setup the uv virtual envirounment using following command in CMD:

uv venv

After the activate this using the follow script:

.venv\Scripts\activate

Now basic project setup is ready for work

Now create a python file named as agent_hello.py in src/hello_agent folder this is the main folder where project files are stored.
 
# Installing the Necessory Dependences 
There are three main dependences that required to run this project: 
1 - OpenAi SDK (For Agent Creation)
2 - dotenv module (To load .env file)
3 - os module (To load api key from .env file from operating system)

To install these in project dependencies use following commands:
1 - uv add openai-agents        (For Agent SDK)
2 - uv add dotenv               (For dotenv module)
3 - os modules comes with python standard package

# Step 2: Creating the "Hello World" Agent Using OpenAi SDK with Google Gemini as LLM
The steps to create an Ai Agent using OpenAI SDK with Google Gemini are as follow:

First we import the following:
1- (Agent, Runner, set_default_openai_client, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled) from agents
2 - load_env from dotenv
3 - import os

Now we perform the following steps:
### 1 - Passing API key and Base Url:
Before running the agent we need to connect it with the desired LLM for this purpose we need to connect it with API key and Pass the baseurl of LLM.
API key is the unique key that is used to connect the agent with LLM .The api key is stored in the .env as this key is kept secret. We load this using dotenv module of python.
The Base Url specifies the root endpoint for the API
As we are using 3rd party LLM (Google Gemini) in this case we get API for AI Studio and baseurl 
By searching openai gemini compatibility on google search bar or by using the following url (https://ai.google.dev/gemini-api/docs/openai) get the baseurl link from there.                                   

### 2 - Change the default openai client:
As we are using external client so we need to change default openai client and provide the client details of LLM we use in this case we use google gemini api key and baseurl in AsyncOpenAI() these are then stored in external_client(variable). And used later on.

### 3 -  Turn off Tracing option:
As we are using 3rd party LLM to connect with openai sdk, we first check if LLM provides the tracing option or not. If LLM provides a tracing option we need to check if it is supported by SDK or not.
In this case we are turning the tracing option off by setting set_tracing_disabled(True). 

### 4 - OpenAIChatCompletionsModel (Model that agent will use to perform task):
To run the agent we need to precisely guide what model to use as well are using Google Gemini but there are different models of so it so set a model variable and pass model as “gemini-2.0-flash” and change openai_client to external_client  in OpenAIChatCompletionsModel 

### 5 - Importing Agent from Agents Module:
Agent is designed to perform specific tasks
(Agent Module Required 3 further things)
	1 - Instructions (Brief details about the task agent will perform)
	2 - Model (the model agent will use to perform the task)
	3 - Agent Name (Role for Agent)
### 6 - Import Runner from Agents Module:
The Runner manages the execution flow of agents
(Runner Module Requires)
	1 - run_sync (this method performs the task in synchronized way )
	2 - Agent (that will perform task)
	3 - Prompt (what user wants to do)

# Step 3: Running the "Hello World" Agent
To run the agent, we first set up a script in the .toml file. The format of the script entry is as follows:
agent = "hello_agent.agent_hello:my_first_agent"

In this line:
    "agent" is the script name.
After the equal sign:
    1 - hello_agent is the folder name,
    2 - agent_hello is the Python file name (without the .py extension),
    3 - my_first_agent is the function that will be executed to run the agent.

To run this agent simply use following command in CMD:
uv run agent


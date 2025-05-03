# import the required openai modules to create Agent 
from agents import ( Agent, Runner, set_default_openai_client, AsyncOpenAI, OpenAIChatCompletionsModel, set_tracing_disabled,)

# Import the dotenv and os modules to run .env file 
from dotenv import load_dotenv
import os

# load the api key that is set in .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Setup the provider (3rd party) 
external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai/"
    )

# Changing the default provider (openai to gemini)
set_default_openai_client(external_client)

# Turning of the tracing
set_tracing_disabled(True)

# Setting the model details (3rd party - Gemini)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Creating a function that runs the agent
def my_first_agent():

# Create the agent
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
        model = model,
        )
    
# Create the runner
    result = Runner.run_sync(agent, "say Hello World!")
    print("\n")
    print(result.final_output)
    print("\n")

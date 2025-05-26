from pydantic import BaseModel
from fastapi import FastAPI
import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


# For Simple data Vaidation
class ChatInput(BaseModel):
    message : str
    name : str

# Configuring Agents SDk
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_api, set_default_openai_client
from openai import AsyncOpenAI
external_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GOOGLE_API_KEY"),
)
set_default_openai_client(external_client)
set_default_openai_api("chat_completions")
set_tracing_disabled(True)
agent = Agent(
    name = "FastAPI",
    instructions = "A simple FastAPI agent",
    model = "gemini-2.0-flash"
)

# For Complex data Validation for ChatCompletionAPIs
class Message(BaseModel):
    role: str
    content : str

class ChatCompletionInput(BaseModel):
    message : list[Message]


app = FastAPI()

@app.post("/")
def hello_fastapi(message: ChatInput):
    """
    A simple hello world endpoint. That returns a greeting message.
    """
    return {"message": f"Hello, FastAPI From {message.name}!"}


@app.post("/ChatCompletion")
def hello_chat_completion(message: ChatCompletionInput):
    """
    A simple hello world endpoint. That returns a greeting message.
    """
    # return message
    msg =  message.model_dump()
    return {"message": f"Hello, FastAPI From {msg['message'][0]['role']}, /n {msg['message'][0]['content']}!"}


@app.post("/agent")
async def hello_agent(msg: ChatCompletionInput):
    """
    A simple fastAPI Agent.
    """
    # data = [m.model_dump() for m in msg.message]
    # print(data)
    result = await Runner.run(
        agent,
        msg.model_dump().get("message"),
    )
    return result.final_output
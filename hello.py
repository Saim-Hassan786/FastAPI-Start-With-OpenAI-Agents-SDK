
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def hello_fastapi():
    """
    A simple hello world endpoint.That retruns a greeting message.
    """
    return {"message":"Hello, FastAPI From Saim Hassan Akhtar!"}

# To Run the Above Code Command : uv run fastapi dev hello.py
# OR Direct With Uvicorn
# uvicorn hello:app --reload

@app.post("/post")
def hello_post(message:dict):
    """
    A simple hello world endpoint. That POSTS a greeting message.
    """
    print("DATA RECEIVED")
    print(message)
    return {"message": f"Hello, {message['name']}! From POST"}

# Another Example
@app.post("/post/exp")
def hello_post_exp(message:dict):
    """
    A simple hello world endpoint. That POSTS a greeting message.
    """
    print("DATA RECEIVED")
    return message
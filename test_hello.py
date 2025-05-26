# A simple greeting msg to Test with simple Assert
def greeting():
    return {"message" : "Hello, FastAPI From Saim Hassan Akhtar!"}

# Test the greeting function
assert greeting() == {"message" : "Hello, FastAPI From Saim Hassan Akhtar!"}
print("✅ Assert passed. The greeting is correct.")

# Now Using Pytest to Check the FastAPIs

from fastapi.testclient import TestClient
from hello import app

client = TestClient(app)

def test_hello_api():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI From Saim Hassan Akhtar!"}

# Run It With The Command : pytest
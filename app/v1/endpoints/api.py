from fastapi import FastAPI, Form
from typing import Annotated


app = FastAPI(title="Liberate Labs Chat API",
              contact={
                    "name": "Liberate Labs",
                    "url": "https://liberate-labs.com/",
                    "email": "rakibhosen@liberate-lab.com",
                })


@app.get("/")
async def index():
    """
    this one is used by fastapi.

    """

    return {"message": "Hello from liblab-chat app"}


@app.post("/hello-message/")
async def hello_message(name: Annotated[str, Form()], age: Annotated[int, Form()]):
    """Sends a hello message with name and age.

    Args:
        name (str):Name of the person.
        age (int): Age of the person.

    Returns:
        message: A message with persons `name` and `age`.
    """
    return {"message": f"Hello {name}. your age is {age}"}


@app.post("/v1/endpoints/hello-message2/")
async def hello_message2(name: Annotated[str, Form()], age: Annotated[int, Form()]):
    """Sends a hello message with name and age.

    Args:
        name (str):Name of the person.
        age (int): Age of the person.

    Returns:
        message: A message with persons `name` and `age`.
    """
    return {"message": f"Hello {name}. your age is {age}"}
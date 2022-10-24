import fastapi
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    phone: str
    password: str

app = FastAPI()

users: list[User] = [
    User(name="A", email="B", phone="C", password="D"),
    User(name="a", email="b", phone="c", password="d"),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/{name}")
def get_user(name: str) -> User:
    for user in users:
        if user.name == name:
            return {"name": user.name,
                    "Email": user.email,
                    "Phone": user.phone,
                    }

    raise fastapi.HTTPException(status_code=404, detail=f"User not found for name {name}")

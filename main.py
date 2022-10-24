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
auth/registration RegRequest RegResponse
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users/{name}")
def get_user(name: str) -> User:
    for user in users:
        if user.name == name:
            return user

    raise fastapi.HTTPException(status_code=404, detail=f"User not found for name {name}")


@app.post("/users/")
def create_user(user: User) -> User:
    if user in users:
        raise fastapi.HTTPException(status_code=409, detail=f'User with name {user.name} already exists')
    users.append(user)
    return user
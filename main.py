import fastapi
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str
    phone: str
    password: str

class RegistrationRequest(BaseModel):
    name: str
    email: str
    phone: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

users: list[User] = [
    User(name="A", email="B", phone="C", password="D"),
    User(name="a", email="b", phone="c", password="d"),
]


@app.post("/auth/registration/")
def register_user(reg_req: RegistrationRequest) -> str:
    if reg_req in users:
        raise fastapi.HTTPException(status_code=409, detail=f'User with name {reg_req.name} already exists')
    users.append(reg_req)
    return "User Created!"

@app.post("/auth/login/")
def login_user(log_req: LoginRequest) -> str:
    return "Login Successful!"

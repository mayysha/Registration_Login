import fastapi
from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3


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
    user = getUserFromRegistrationReq(reg_req)
    createNewUserInDb(user)

    return "User Created!"

@app.post("/auth/login/")
def login_user(log_req: LoginRequest) -> str:
    return "Login Successful!"



def getUserFromRegistrationReq(reg_req):
    user = User(name=reg_req.name,email=reg_req.email,phone=reg_req.phone,password=reg_req.password)
    return user
def createNewUserInDb(user):
    sql_command = "INSERT INTO USER (NAME, EMAIL, PHONE, PASSWORD) VALUES ('" +user.name +"','" + user.email +"','"+ user.phone +"','"+ user.password+"')"
    conn = sqlite3.connect('db.db')
    conn.execute(sql_command)
    conn.commit()

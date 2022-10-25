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


@app.post("/auth/registration/")
def register_user(reg_req: RegistrationRequest) -> str:
    user = get_user_from_registration_req(reg_req)
    create_new_user_in_db(user)

    return "User Created!"


@app.post("/auth/login/")
def login_user(log_req: LoginRequest) -> str:
    user = get_user_from_db(log_req.email)
    # validate password (log_req.password, user.password)
    if validate_password(log_req.password, user.password):
        return "Login Successful!"
    else:
        return "User not found! Please Register"


def get_user_from_registration_req(reg_req):
    user = User(name=reg_req.name, email=reg_req.email, phone=reg_req.phone, password=reg_req.password)
    return user


def create_new_user_in_db(user):
    sql_command = "INSERT INTO USER (NAME, EMAIL, PHONE, PASSWORD) VALUES ('" + user.name + "','" + user.email + "','" + user.phone + "','" + user.password + "')"
    conn = sqlite3.connect('db.db')
    conn.execute(sql_command)
    conn.commit()
    conn.close()


def get_user_from_db(email):
    user = User.construct()
    conn = sqlite3.connect('db.db')
    cursor = conn.execute("SELECT name, email, phone,password from USER where email='" + email + "'")
    for row in cursor:
        user.name = row[0]
        user.email = row[1]
        user.phone = row[2]
        user.password = row[3]
    conn.close()
    return user


def validate_password(log_req_password, user_password):
    if log_req_password == user_password:
        return True
    else:
        return False

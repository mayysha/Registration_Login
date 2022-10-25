# User-Registration-and-Login-system


## Prerequisites
- You will need to have Python3
- Setup `virtualenv` and install dependencies from `req.txt`
```console
your_pc$ virtualenv -p /usr/bin/python3 venv
```
```console
your_pc$ source venv/bin/activate
```
```console
(venv)your_pc$ pip install -r req.txt
```
```console
(venv)your_pc$ uvicorn main:app --reload
```

### Requests and Response
    
`http://127.0.0.1:8000/auth/registration/` 

Request Body
```json
{
    "name" :"a",
    "email" : "b",
    "phone" :"c",
    "password" : "d"
}
```
Response Body
```json
"User Created!"
```

`http://127.0.0.1:8000/auth/login/` 

Request Body
```json
{
    "email" : "b",
    "password" : "d"
}

```
Response Body
```json
"Login Successful!"
```

### Project Organization

    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── db.db              <- Database
    │
    ├── req.txt            <- The requirements file for python environment
    │
    │── .gitignore         <- you know what this is :P
    │
    ├── main.py            <- contains the python script


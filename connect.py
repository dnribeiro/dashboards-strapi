import requests as req
from dotenv import load_dotenv
import os
import json
load_dotenv()
strapi_key = os.getenv('STRAPI_KEY')
email = os.getenv('EMAIL')
password = os.getenv('PWD')

def connect():
    res = req.post(

    "http://172.19.240.45:7834/admin/login", 

    data = { 

    'email' : f'{email}', 

    'password' : f'{password}' , 

    'Content-Type' : "application/json"

    }).json()["data"]
    res

def get(table, id):
    return req.get(

    f"http://172.19.240.28:7834/api/{table}/{id}", 

    headers = {"Authorization": f"Bearer {strapi_key}"}

    ).json()

def get_all(table):
    return req.get(

    f"http://172.19.240.28:7834/api/{table}", 

    headers = {"Authorization": f"Bearer {strapi_key}"}

    ).json()
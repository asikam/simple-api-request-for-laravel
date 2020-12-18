import os
import requests
import json
import settings
import sys


url = os.getenv("LARAVEL_URL")+"/oauth/token"

myobj = {
    "grant_type" : "password",
    "client_id" : os.getenv("CLIENT_ID"),
    "client_secret" :  os.getenv("CLIENT_SECRET"),
    "username" : os.getenv("CLIENT_USERNAME"),
    "password" : os.getenv("CLIENT_PASSWORD"),
    "scope" : ""
    }

x = requests.post(url, data = myobj)

response = x.json()

token = response['token_type'] + ' ' + response['access_token']

user_url = os.getenv("LARAVEL_URL")+"/api/user"
headers = {
    "Accepts" : "application/json",
    "Authorization" : token
    }

user = requests.get(user_url,headers = headers)


print(user.json()['name']+ "   " +user.json()['email'])

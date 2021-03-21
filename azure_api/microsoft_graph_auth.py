import json
import requests
import pandas as pd
import pyodbc


def get_token():
	with open("../auth.json","r") as f:
		auth_details = json.load(f)

	token_url = f"https://login.microsoftonline.com/{auth_details['Overview']['Tenant ID']}/oauth2/token"

	app_id = auth_details["Overview"]["Application ID"]
	client_secret = auth_details["Certificates & Secrets"]["Value"]

	token_data = {
		"grant_type": "password",
		"client_id": app_id,
		"client_secret": client_secret,
		"resource": "https://graph.microsoft.com",
		"scope": "https://graph.microsoft.com",
		"username": "maat1@st-andrews.ac.uk",
		"password": "This__way__202"
	}

	token_request = requests.post(token_url,data=token_data)
	token = token_request.json().get("access_token")

	print(token_request.content)



get_token()



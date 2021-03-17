from typing import Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from dateutil import tz, parser
from tutorial.auth_helper import *
from tutorial.graph_helper import *

def initialize_context(request) -> Dict:
	context = {}

	# Check fo any erros in the session
	error = request.session.pop("flash_error",None)

	if error!=None:
		context["errors"] = []
		context["errors"].append(error)

	context["user"] = request.session.get("user",{"is_authenticated":False})
	return context
		

def home(request):
	context = initialize_context(request)
	return render(request,"tutorial/home.html",context)

def sing_in(request):
	flow = get_sign_in_flow()
	try:
		request.session["auth_flow"] = flow
	except Exception as e:
		print(e)
	
	return HttpResponseRedirect(flow["auth_uri"])

def callback(request):
	result = get_token_from_code(request)

	user = get_user(result["access_token"])

	request.session['flash_error'] = { 'message': 'Token retrieved', 'debug': 'User: {0}\nToken: {1}'.format(user, result) }

	store_user(request,user)
	return HttpResponseRedirect(reverse(home))

def sign_out(request):
	remove_user_and_token(request)

	return HttpResponseRedirect(reverse("home"))
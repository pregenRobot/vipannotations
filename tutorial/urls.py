from django.urls import path

from . import views

urlpatterns = [
	path("",views.home, name="home"),
	path("signin",views.sing_in, name = "signin"),
	path("signout",views.sign_out, name = "singout"),
	path("calendar", views.home, name = "calendar"),
	path("callback",views.callback, name="callback")
]
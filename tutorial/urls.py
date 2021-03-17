from django.urls import path

from . import views

urlpatterns = [
	path("",views.home, name = "home"),
	path("signin",views.home, name="signin"),
	path("calendar",views.home, name="calendar")
]
from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^$',Login,name="Login"),
		url(r'^Register/$',Register,name="Register"),
		url(r'^Index/$',Index,name="Index"),
	]
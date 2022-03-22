from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Create_Company$',Create_Company,name="Create_Company"),
		url(r'^Create_Client$',Create_Client,name="Create_Client"),
		url(r'^Create_Invoice_$',Create_Invoice_,name="Create_Invoice_"),
	]
from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Electronic_Invoice_List$',Electronic_Invoice_List,name="Electronic_Invoice_List"),
	]
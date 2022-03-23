from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^List_Invoice/$',List_Invoice,name="List_Invoice"),
		url(r'^Create_Invoice/$',Create_Invoice,name="Create_Invoice"),
	]
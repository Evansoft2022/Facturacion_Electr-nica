from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
# from .serializer import *
import base64
from .Create_Company import CreateCompany
from .Create_Client import CreateClient
from .Create_Category import Create_Category_
from .Create_Inventory import CreateInventory
from .Create_Invoice import *
from django.utils.crypto import get_random_string

@api_view(['POST'])
def Create_Company(request):
	data = request.data
	token = get_random_string(length=96)
	passwd = get_random_string(length=96)
	c = CreateCompany(data,token,passwd)
	message = c.Create()
	_message = {'Message':message}
	if message == "Successfully registered company":
		_message = {'Message':message,'Token':token,'Passwd':passwd}
	return Response(_message)

@api_view(['POST'])
def Create_Client(request):
	data = request.data
	c = CreateClient(data)
	message = c.Create()
	return Response({'Message':message})

@api_view(['POST'])
def Create_Invoice_(request):
	data = request.data
	c = CreateInvoice(data)
	c.Create_Invoice_Lines()
	message = c.Create_Payment_Form()
	return Response({'Message':message})


@api_view(['POST'])
def Create_Payroll(request):
	data = request.data
	return Response({'Message':data})

@api_view(['POST'])
def Create_Category(request):
	data = request.data
	c = Create_Category_(data)
	message = c.Create()
	return Response({'Message':message})


@api_view(['POST'])
def Create_Inventory(request):
	data = request.data
	c = CreateInventory(data)
	message = c.Create()
	return Response({'Message':message})

@api_view(['POST'])
def Create_Empleoyee(request):
	data = request.data
	message = ""
	return Response({'Message':message})
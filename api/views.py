from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
# from .serializer import *
import base64
from .Create_Company import CreateCompany
from .Create_Client import CreateClient
from .Create_Invoice import *
from django.utils.crypto import get_random_string

@api_view(['POST'])
def Create_Company(request):
	data = request.data
	token = get_random_string(length=96)
	c = CreateCompany(data,token)
	message = c.Create()
	return Response({'Message':message,'Token':token})

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





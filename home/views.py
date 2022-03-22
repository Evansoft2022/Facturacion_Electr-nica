from django.shortcuts import render
from company.models import Company

def Login(request):
	return render(request,'home/login.html')

def Register(request):
	return render(request,'home/register.html')	



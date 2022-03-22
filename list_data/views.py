from django.http import HttpResponse
from django.shortcuts import render
from invoice.models import *
from company.models import Company
from client.models import Client
from api.translator import Translator
import time

t = Translator()

def Electronic_Invoice_List(request):
	start = time.time()
	company = Company.objects.get(documentIdentification = t.codificar(str('20302968')))
	invoice = Invoice.objects.filter(company = company)
	print(invoice)
	print('\nTermino en ',time.time() - start)
	return render(request,'mounting.html',{'invoice':invoice})




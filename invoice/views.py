from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from api.translator import Translator
import time, threading, queue
from client.models import Client

t = Translator()
my_queue = queue.Queue()

def storeInQueue(f):
  def wrapper(*args):
  	global my_queue
  	my_queue.put(f(*args))
  return wrapper

@storeInQueue
def Invoice_Data(request):
	_invoice = Invoice.objects.filter(company = Company.objects.get(documentIdentification = t.codificar(str(20302968))))
	invoice = []
	start = time.time()
	data = [
			{
				'pk':i.pk,
				'number':t.decodificar(str(i.prefix))+'-'+t.decodificar(str(i.number)),
				'date':t.decodificar(str(i.date)),
				'client':t.decodificar(str(i.client.name)),
				'state':"Sin enviar a la DIAN"
			} 
			for i in _invoice
			]
	print("Terminado",time.time() - start)
	return data

def List_Invoice(request):	
	u = threading.Thread(target=Invoice_Data,args=(request,), name='PDF')
	u.start()
	data = my_queue.get()
	return render(request,'fe/list_invoice.html',{'invoice':data})

def Create_Invoice(request):
	client = Client.objects.filter(company = Company.objects.get(documentIdentification=t.codificar(str(20302968))))
	Inventory = Client.objects.filter(company = Company.objects.get(documentIdentification=t.codificar(str(20302968))))
	if request.is_ajax():
		request.session['client'] = request.GET.get("pk")
		return HttpResponse(request.GET.get("pk"))
	data_client = [
									{'name':t.decodificar(str(i.name)),'pk':i.pk}
									for i in client
								]

	return render(request,'fe/create_invoice.html',{'client':data_client})
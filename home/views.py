from django.shortcuts import render
from company.models import Company
from api.translator import Translator
from invoice.models import Invoice
t = Translator()

def Login(request):
	if request.method == 'POST':
		try:
			company = Company.objects.get()
		except Exception as e:
			raise e
	return render(request,'home/login.html')

def Register(request):
	return render(request,'home/register.html')	

def Index(request):
	return render(request,'home/index.html',{
												'invoice':len(Invoice.objects.filter(company = Company.objects.get( documentIdentification =t.codificar(str(20302968)))))
											}
				)



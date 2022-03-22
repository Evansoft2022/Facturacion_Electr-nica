from django.db import models
from data.models import *
from api.translator import Translator


t = Translator()

class Company(models.Model):
	documentIdentification = models.TextField(unique = True)
	type_documentI = models.ForeignKey(Type_Document_Identification,on_delete = models.CASCADE)
	type_organization = models.ForeignKey(Type_Organization,on_delete=models.CASCADE)
	type_regime = models.ForeignKey(Type_Regime,on_delete=models.CASCADE)
	business_name = models.TextField()
	municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE)
	address = models.TextField()
	phone = models.TextField()
	email = models.TextField()
	certificate_generation_date = models.CharField(max_length=10)
	certificate_expiration_date = models.CharField(max_length=10)
	resolution_generation_date = models.CharField(max_length=10)
	resolution_expiration_date = models.CharField(max_length=10,default="")
	block = models.BooleanField(default = False)
	token = models.TextField(default = "" )

	def __str__(self):
		name = t.decodificar(self.business_name)
		return name




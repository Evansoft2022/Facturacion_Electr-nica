from django.db import models
from company.models import Company
from api.translator import Translator

t = Translator()

class Category(models.Model):
	name = models.TextField(unique = True)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,null = True)

	def __str__(self):
		return t.decodificar(str(self.name))




class Inventory(models.Model):
	code = models.TextField(unique = True)
	name = models.TextField()
	quanty = models.TextField()
	price = models.TextField()
	tax = models.TextField()
	initial_inventory = models.TextField()
	exhausted = models.BooleanField(default=False)
	category = models.ForeignKey(Category,on_delete = models.CASCADE,null=True,default=1)
	company = models.ForeignKey(Company,on_delete=models.CASCADE,null = True)

	def __str__(self):
		return t.decodificar(str(self.name))


class Record(models.Model):
	code = models.TextField()
	quanty = models.TextField()
	price = models.TextField()
	tax = models.TextField()
	client = models.TextField()
	empleoyee = models.TextField()
	date = models.TextField()
	time = models.TextField()





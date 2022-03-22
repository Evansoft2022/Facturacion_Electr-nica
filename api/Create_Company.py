from company.models import *
from data.models import *
from api.translator import Translator
from data.models import *

t = Translator()

class CreateCompany:

	def __init__(self,data,token):
		self.data = data
		self.token = token

	def Create(self):
		try:
			Company(
				documentIdentification = t.codificar(str(self.data['document_identification'])),
				type_documentI = Type_Document_Identification.objects.get(_id = self.data['type_document_identification_id']),
				type_organization = Type_Organization.objects.get(_id = self.data['type_organization_id']),
				type_regime = Type_Regime.objects.get(_id = self.data['type_regime_id']),
				business_name = t.codificar(str(self.data['business_name'])),
				municipality = Municipality.objects.get(_id = self.data['municipality_id']),
				address = t.codificar(str(self.data['address'])),
				phone = t.codificar(str(self.data['phone'])),
				email = t.codificar(str(self.data['email'])),
				certificate_generation_date = self.data['certificate_generation_date'],
				certificate_expiration_date = self.data['certificate_expiration_date'],
				resolution_generation_date = self.data['resolution_generation_date'],
				resolution_expiration_date = self.data['resolution_expiration_date'],
				token = t.codificar(str(self.token))
			).save()
			return "Successfully registered company"
		except Exception as e:
			return "The company already exists"
		


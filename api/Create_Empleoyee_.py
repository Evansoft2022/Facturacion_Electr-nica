from .translator import Translator
from company.models import Company

class CreateEmpleoyee:
	def __init__(self,data):
		self.data = dat

	def Create(self,passwd):
		try:
			pass
		except Exception as e:
			raise e


	def Validate(self):
		value = False
		for i in self.data:
			if self.data['second_surname'] != "" or self.data['second_surname'] == "":
				pass
			else:
				if self.data[i] == "" or self.data[i] == None:
					return False


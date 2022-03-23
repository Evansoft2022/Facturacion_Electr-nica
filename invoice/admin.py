from django.contrib import admin
from .models import *

admin.site.register(Invoice)
admin.site.register(Payment_Form_Invoice)
admin.site.register(Consecutive_POS)
admin.site.register(Consecutive_Elec)

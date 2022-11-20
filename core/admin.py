from django.contrib import admin

from .models import Customer, PaymentsCustomer

admin.site.register(Customer)
admin.site.register(PaymentsCustomer)
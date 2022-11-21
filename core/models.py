import uuid
from django.db import models


class Customer(models.Model):
    """A model for Customer table"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    paternal_surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('can_add_customer', 'can add customer'),
            ('can_edit_customer', 'can edit customer propperties'),
            ('can_delete_customer', 'can delete customer'),
        ]


class PaymentsCustomer(models.Model):
    """A model for Payments Table"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    class Meta:
        permissions = [
            ('can_edit_payment', 'can edit payment propperties'),
            ('can_delete_payment', 'can delete payment'),
        ]

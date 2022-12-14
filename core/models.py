import random
import uuid
from django.db import models
from django.db.models.signals import post_save


class Customer(models.Model):
    """A model for Customer table"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    paternal_surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name


class PaymentsCustomer(models.Model):
    """A model for Payments Table"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


def create_dummy_payments_signal(sender, instance, **kwargs):
    payments_count = random.randint(1, 9)
    customer = instance

    for payment in range(0, payments_count):
        random_amount = random.randint(20, 5000)
        random_quantity = random.randint(1,20)

        PaymentsCustomer.objects.create(
            product_name=f"Pago {payment}",
            amount=random_amount,
            quantity=random_quantity,
            customer=customer
        )

post_save.connect(create_dummy_payments_signal, sender=Customer)

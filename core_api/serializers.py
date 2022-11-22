from rest_framework import serializers

from core.models import Customer, PaymentsCustomer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'paternal_surname', 'email')
        read_only_fields = ['id']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsCustomer
        fields = ('id', 'amount', 'product_name', 'quantity', 'customer')
        read_only_fields = ['id', 'customer']

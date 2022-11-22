from rest_framework import generics

from core.models import Customer, PaymentsCustomer
from . import serializers


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


class PaymentList(generics.ListCreateAPIView):
    queryset = PaymentsCustomer.objects.all()
    serializer_class = serializers.PaymentsSerializer


class PaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentsCustomer.objects.all()
    serializer_class = serializers.PaymentsSerializer

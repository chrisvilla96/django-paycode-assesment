from rest_framework import viewsets, permissions

from core.models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomerSerializer
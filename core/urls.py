from django.urls import path

from .views import IndexView, CustomerDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('customer/<uuid:pk>', CustomerDetailView.as_view(), name='customer-detail'),
]
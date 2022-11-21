from django.urls import path

from .views import HomeView, IndexView, CustomerDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('index/', IndexView.as_view(), name='index'),
    path('customer/<uuid:pk>', CustomerDetailView.as_view(), name='customer-detail'),
]
from django.urls import path

from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('customer/<uuid:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('customer/create', views.CustomerCreateView.as_view(), name='create-customer')
]
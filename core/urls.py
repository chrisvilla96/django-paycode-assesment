from django.urls import path

from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('customer/<uuid:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('customer/create', views.CustomerCreateView.as_view(), name='customer-create'),
    path('customer/update/<uuid:pk>',views.CustomerUpdateView.as_view(), name='customer-update'),
    path('customer/delete/<uuid:pk>',views.CustomerDeleteView.as_view(), name='customer-delete'),
]
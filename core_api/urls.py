from rest_framework import routers 
from django.urls import path

from . import views

urlpatterns = [
    path('customers/', views.CustomerList.as_view()),
    path('customers/<uuid:pk>', views.CustomerDetail.as_view()),
    path('payments/', views.PaymentList.as_view()),
    path('payments/<uuid:pk>', views.PaymentDetail.as_view()),
]
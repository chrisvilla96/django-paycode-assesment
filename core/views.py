from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import Customer

class HomeView(TemplateView):
    """View for Home"""

    template_name = 'home.html'


class IndexView(LoginRequiredMixin, ListView):
    """View for index"""

    template_name = "index.html"
    model = Customer
    login_url = '/login/'


class CustomerDetailView(LoginRequiredMixin, DetailView):
    """View for Customer Details"""

    template_name = "customer-detail.html"
    model = Customer
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs['pk']
        context["payments"] = Customer.objects.get(pk=customer_id).paymentscustomer_set.all()
        return context


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """View for creating Customers"""

    permission_required = 'core.add_customer'

    template_name = 'customer/customer-create.html'
    model = Customer
    fields = ['name', 'paternal_surname', 'email']
    success_url = '/index/'


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """View for editing Customers"""

    permission_required = 'core.change_customer'

    template_name = 'customer/customer-edit.html'
    model = Customer
    fields = ['name', 'paternal_surname', 'email']
    success_url = '/index/'


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """View for deleting Customer"""

    permission_required = 'core.delete_customer'

    template_name = 'customer/customer-delete.html'
    model = Customer
    success_url = '/index/'

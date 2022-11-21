from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView

from .models import Customer, PaymentsCustomer


class HomeView(TemplateView):
    """View for Home"""

    template_name = 'home.html'


class IndexView(ListView):
    """View for index"""

    template_name = "index.html"
    model = Customer


class CustomerDetailView(DetailView):
    """View for Customer Details"""

    template_name = "customer-detail.html"
    model = Customer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs['pk']
        context["payments"] = Customer.objects.get(pk=customer_id).paymentscustomer_set.all()
        return context
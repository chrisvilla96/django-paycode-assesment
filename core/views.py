from django.views.generic import ListView

from .models import Customer

class IndexView(ListView):
    """View for index"""

    template_name = "index.html"
    model = Customer


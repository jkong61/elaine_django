from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Instance, NDECertificate

# Create your views here.

class HomePageView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Instance
    context_object_name = 'instance_list'
    template_name = 'core/index.html'

    def get_queryset(self):
        queryset = Instance.objects.all()
        return queryset
    
    # Method to add context to the TemplateView
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return context
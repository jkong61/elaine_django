from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomePageView(LoginRequiredMixin,TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'core/index.html'
    
    # Method to add context to the TemplateView
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        return context
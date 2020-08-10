from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Instance, NDECertificate
import datetime
from elaine.settings import INSTANCES_CHECKED

# Create your views here.

class HomePageView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    model = Instance
    context_object_name = 'instance_list'
    template_name = 'core/index.html'

    #  Overriden method to get the query set
    def get_queryset(self):
        if ('q' in self.request.GET and self.request.GET['q'] == 'all'):
            # TODO refine the all search
            # view all NDE where Certificates are actively in use
            return NDECertificate.objects.filter(in_use = True).filter(validity=True)
        return NDECertificate.objects.filter(validity = False)
    
    # Method to add context to the TemplateView
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['date_today'] = datetime.date.today().strftime('%B %d, %Y')
        return context

    def get(self, request, *args, **kwargs):
        global INSTANCES_CHECKED
        if(not INSTANCES_CHECKED):
            queryset = NDECertificate.objects.filter(validity=True)
            for item in queryset:
                item.checkexpiry()
            # INSTANCES_CHECKED = True

        return super().get(request, *args, **kwargs)

class NDEFormsView(LoginRequiredMixin,TemplateView):
    template_name = 'core/nde_forms.html'
    login_url = reverse_lazy('login')

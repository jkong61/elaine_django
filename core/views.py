from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, ListView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from inspection.models import SkidVisualInspection
from .forms import GenericInstanceForm
import datetime
from elaine.settings import INSTANCES_CHECKED

# Create your views here.

class HomePageView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    context_object_name = 'instance_list'
    template_name = 'core/index.html'

    #  Overriden method to get the query set
    def get_queryset(self):
        if ('q' in self.request.GET and self.request.GET['q'] == 'all'):
            # view all NDE where Certificates are actively in use
            return SkidVisualInspection.objects.exclude(validity = False)
        return SkidVisualInspection.objects.filter(in_use = True).filter(validity=True)
    
    # Method to add context to the TemplateView
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['date_today'] = datetime.date.today().strftime('%B %d, %Y')
        return context

    def get(self, request, *args, **kwargs):
        global INSTANCES_CHECKED
        if(not INSTANCES_CHECKED):
            queryset = SkidVisualInspection.objects.filter(validity=True)
            for item in queryset:
                item.checkexpiry()
            # INSTANCES_CHECKED = True

        return super().get(request, *args, **kwargs)

class InstanceCreationView(LoginRequiredMixin, FormView):
    form_class = GenericInstanceForm
    template_name = 'core/add_form.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('core-success')

    def form_valid(self, form):
        id = form.cleaned_data.get('multifield').material_type.description
        if(id == 'Pipework'):
            print(1)
        elif(id == 'Skid'):
            print(2)
        elif(id == 'Sling'):
            print(3)
        else:
            print('TMMDE')
        print(self.request.POST)
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = 'core/success.html'
from django.shortcuts import render
from .models import CalibrationInspection
from .forms import GenericInspectionForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

# Create your views here.
class InspectionCreateView(FormView):
    form_class = GenericInspectionForm
    template_name = 'inspection/add.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Inspection'
        context['header'] = 'Add Inspection Certificate'
        return context

    def form_valid(self, form):
        print(self.request.POST)
        return super().form_valid(form)

    def form_invalid(self, form):
        print(self.request.POST)
        return super().form_invalid(form)
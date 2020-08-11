from django.shortcuts import render
from .models import CalibrationInspection
from .forms import CalibrationInspectionForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

# Create your views here.
class CalibrationCreateView(FormView):
    model = CalibrationInspection
    form_class = CalibrationInspectionForm
    template_name = 'inspection/add.html'

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Calibration Inspection'
        context['header'] = 'Calibration Certification'
        return context
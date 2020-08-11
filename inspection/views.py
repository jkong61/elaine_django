from django.shortcuts import render
from .models import CalibrationInspection
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
class CalibrationCreateView(CreateView):
    model = CalibrationInspection
    fields = ['validity_start_date','material_instance']
    template_name = 'inspection/add.html'
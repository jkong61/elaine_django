from django import forms
from core.models import Instance
from .models import VisualInspection, MPIInpection, PipeworkNDEInspection, AnnualInspection, MajorInspection, PrePostJobInspection, CalibrationInspection

class GenericInspectionForm(forms.ModelForm):
    class Meta:
        fields = ['validity_start_date','validity','in_use']
        read_only = ['validity_end_date']

class CalibrationInspectionForm(GenericInspectionForm):
    class Meta(GenericInspectionForm.Meta):
        model = CalibrationInspection
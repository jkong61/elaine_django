from django.forms import ModelForm
from .models import VisualInspection, MPIInpection, PipeworkNDEInspection, AnnualInspection, MajorInspection, PrePostJobInspection, CalibrationInspection

class GenericInspectionForm(ModelForm):
    class Meta:
        fields = ['validity_start_date','material_instance','validity','in_use']
        read_only = ['validity_end_date']

class CalibrationInspectionForm(GenericInspectionForm):
    class Meta(GenericInspectionForm.Meta):
        model = CalibrationInspection
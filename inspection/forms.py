from django import forms
from core.models import Instance, TMMDEInstance
from .models import SkidVisualInspection, SkidMPIInpection, SlingMPIInpection, SlingVisualInspection, PipeworkNDEInspection, AnnualInspection, MajorInspection, PrePostJobInspection, CalibrationInspection

class GenericInspectionForm(forms.Form):

    MODEL_CHOICES = [
        ('', 'Select an inspection type'),
        ('sv', SkidVisualInspection._meta.verbose_name),
        ('sm', SkidMPIInpection._meta.verbose_name),
        ('slv', SlingVisualInspection._meta.verbose_name),
        ('slm', SlingMPIInpection._meta.verbose_name),
        ('pnde', PipeworkNDEInspection._meta.verbose_name),
        ('pann', AnnualInspection._meta.verbose_name),
        ('pmaj', MajorInspection._meta.verbose_name),
        ('pppj', PrePostJobInspection._meta.verbose_name),
        ('tmde', TMMDEInstance._meta.verbose_name),
    ]

    validity_start_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}))
    validity_end_date = forms.DateField(disabled=True)
    validity = forms.BooleanField(initial=True,help_text="Is inspection valid?")
    in_use = forms.BooleanField(initial=True,help_text="Is inspection in use?")
    model_select = forms.ChoiceField(choices=MODEL_CHOICES, label="Inspection type",initial='')


    class Meta:
        fields = ['validity_start_date','validity_end_date','material_instance','validity','in_use']

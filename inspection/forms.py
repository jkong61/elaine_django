from django import forms
from .models import SkidVisualInspection, SkidMPIInpection, SlingMPIInpection, SlingVisualInspection, PipeworkNDEInspection, AnnualInspection, MajorInspection, PrePostJobInspection, CalibrationInspection


class AjaxChoiceField(forms.ChoiceField):
    def valid_value(self, value):
        return True

class GenericInspectionForm(forms.Form):

    MODEL_CHOICES = [
        ('', 'Select an inspection type'),
        ('skv', SkidVisualInspection._meta.verbose_name),
        ('skm', SkidMPIInpection._meta.verbose_name),
        ('slv', SlingVisualInspection._meta.verbose_name),
        ('slm', SlingMPIInpection._meta.verbose_name),
        ('pwpnde', PipeworkNDEInspection._meta.verbose_name),
        ('pwann', AnnualInspection._meta.verbose_name),
        ('pwmaj', MajorInspection._meta.verbose_name),
        ('pwppj', PrePostJobInspection._meta.verbose_name),
        ('tmde', CalibrationInspection._meta.verbose_name),
    ]

    model_select = forms.ChoiceField(choices=MODEL_CHOICES, label="Inspection type",initial='')
    instance_select = AjaxChoiceField(label="Equipment Instance",initial='')
    validity_start_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}))
    validity_end_date = forms.DateField(disabled=True)
    validity = forms.BooleanField(initial=True,help_text="Is inspection valid?")
    in_use = forms.BooleanField(initial=True,help_text="Is inspection in use?")

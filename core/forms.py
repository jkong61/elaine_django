from django import forms
from .models import Instance, Material, PipeworkInstance, SkidInstance, SlingInstance, TMMDEInstance

class GenericInstanceForm(forms.Form):
    multifield = forms.ModelChoiceField(queryset=Material.objects.all(),empty_label='Select Material',label='Material Number',to_field_name='material_type')

    class Meta:
        fields = ['multifield']
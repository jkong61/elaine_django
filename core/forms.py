from django import forms
from .models import Material, JobLocation, PipeworkInstance, SkidInstance, SlingInstance, TMMDEInstance

class GenericInstanceForm(forms.Form):
    multifield = forms.ModelChoiceField(queryset=Material.objects.all(),empty_label='Select Material',label='Material Number',to_field_name='material_type')
    serial_number = forms.CharField(max_length="255",required=True)
    allocation = forms.ModelChoiceField(queryset=JobLocation.objects.all(),empty_label='Select Allocation',label='Job Location',required=False)
    class Meta:
        fields = ['multifield', 'serial_number','allocation']

    def is_valid(self):
        valid = super(GenericInstanceForm ,self).is_valid()
        if(valid):
            cd = self.cleaned_data
            material = cd.get('multifield')
            data = {
                'material' : cd.get('multifield'),
                'serial_number' : cd.get('serial_number'),
                'instance_allocation' : cd.get('allocation')
            }
            desc = material.material_type.description
            if(desc == 'Pipework'):
                item = PipeworkInstance
            elif(desc == 'Skid'):
                item = SkidInstance
            elif(desc == 'Sling'):
                item = SlingInstance
            else:
                item = TMMDEInstance
            self.create_object(item, data)
            return True
        else:
            return False

    def create_object(self, item, data):
        instance = item.objects.create(**data)
        self.object_id = instance.id

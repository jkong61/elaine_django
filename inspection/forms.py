from core.models import PipeworkInstance, SkidInstance, SlingInstance, TMMDEInstance
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
    validity_end_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}))
    validity = forms.BooleanField(initial=True,help_text="Is inspection valid?")
    in_use = forms.BooleanField(initial=True,help_text="Is inspection in use?")

    def is_valid(self):
        valid = super(GenericInspectionForm ,self).is_valid()
        if(valid):
            cd = self.cleaned_data
            inspection_type= cd['model_select']
            if(inspection_type[:2] == 'sk'):
                model = SkidInstance
                if(inspection_type == 'skv'):
                    model_used = SkidVisualInspection
                else:
                    model_used = SkidMPIInpection
            elif(inspection_type[:2] == 'sl'):
                model = SlingInstance
                if(inspection_type == 'slv'):
                    model_used = SlingVisualInspection
                else:
                    model_used = SlingMPIInpection
            elif(inspection_type[:2] == 'pw'):
                model = PipeworkInstance
                if(inspection_type == 'pwpnde'):
                    model_used = PipeworkNDEInspection
                elif(inspection_type == 'pwann'):
                    model_used = AnnualInspection
                elif(inspection_type == 'pwmaj'):
                    model_used = MajorInspection
                else:
                    model_used = PrePostJobInspection
            else:
                model = TMMDEInstance
                model_used = CalibrationInspection
                
            data = {
                'material_instance' : model.objects.get(id__exact = cd.get('instance_select')),
                'validity_start_date' : cd.get('validity_start_date'),
                'validity_end_date' : cd.get('validity_end_date'),
                'validity' : cd.get('validity'),
                'in_use' : cd.get('in_use'),
            }

            # Create the certificate
            self.__invalidate_old_cert(model_used)            
            self.create_object(model_used, data)
            return True
        else:
            return False


    def create_object(self, item, data):
        instance = item.objects.create(**data)
        self.object_id = instance.id
        self.object_type = item

    def __invalidate_old_cert(self,item):
        cert = item.objects.filter(in_use = True, validity = True).first()
        if(cert):
            cert.in_use = False
            cert.validity = False
            cert.save()
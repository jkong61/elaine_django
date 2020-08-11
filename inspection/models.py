from django.db import models
from core.models import PipeworkInstance, SkidInstance, SlingInstance, TMMDEInstance
import datetime
import uuid

WARNING_WINDOW_WEEKS = 6

# Create your models here.
# Inspections tied to an Instance:
class Inspection(models.Model):
    id = models.UUIDField('ID',default=uuid.uuid4,primary_key=True,unique=True,help_text="Unique ID for Material Instance")
    validity_start_date = models.DateField('Start Date',null=True)
    validity_end_date = models.DateField('Expiry Date',null=True)
    validity = models.BooleanField('Inspection Valid', default=True, help_text="Is the inspection valid?")
    in_use = models.BooleanField('Inspection In Use', default=True, help_text="Is the inspection in use?")

    class Meta():
        abstract = True
        verbose_name = "Inspection"

    def __str__(self):
        return f'{self.id}'

    def checkexpiry(self):
        instance = self.get_reference_material()
        if(self.validity_end_date < datetime.date.today()):
            self.validity = False
            self.save()
            instance.set_expire()
            return 'Expired'
        elif(self.validity_end_date <= (datetime.date.today() + datetime.timedelta(weeks=WARNING_WINDOW_WEEKS))):
            return 'Expiring'
        return 'Valid'

    def get_inspection_status(self):
        instance = self.get_reference_material()
        if(self.validity_end_date < datetime.date.today()):
            return 'Expired'
        elif(self.validity_end_date <= (datetime.date.today() + datetime.timedelta(weeks=WARNING_WINDOW_WEEKS))):
            return 'Expiring'
        return 'Valid'

    def get_time_left_days(self):
        if(self.validity_end_date > datetime.date.today()):
            timedelta = self.validity_end_date - datetime.date.today()
            return timedelta.days
        else:
            return 0

    def set_not_in_use(self):
        self.in_use = False
        self.save()


# Lifting related inspections
class AbstractSkidInspection(Inspection):
    material_instance = models.ForeignKey('core.SkidInstance', on_delete=models.CASCADE, null=True)
    class Meta:
        abstract = True

    def get_reference_material(self):
        return SkidInstance.objects.get(id=self.material_instance.id)

class SkidVisualInspection(AbstractSkidInspection):
    
    class Meta:
        verbose_name_plural = "Skid Visual Inspections"
        verbose_name = "Skid Visual Inspection"

class SkidMPIInpection(AbstractSkidInspection):

    class Meta:
        verbose_name_plural = "Skid MPI Inspections"
        verbose_name = "Skid MPI Inspection"

class AbstractSlingInspection(Inspection):
    material_instance = models.ForeignKey('core.SlingInstance', on_delete=models.CASCADE, null=True)
    class Meta:
        abstract = True

    def get_reference_material(self):
        return SlingInstance.objects.get(id=self.material_instance.id)

class SlingVisualInspection(AbstractSlingInspection):
    
    class Meta:
        verbose_name_plural = "Sling Visual Inspections"
        verbose_name = "Sling Visual Inspection"

class SlingMPIInpection(AbstractSlingInspection):

    class Meta:
        verbose_name_plural = "Sling MPI Inspections"
        verbose_name = "Sling MPI Inspection"        


# Measuring and Monitoring equipment inspections
class CalibrationInspection(Inspection):
    material_instance = models.ForeignKey('core.TMMDEInstance', on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = 'Calibration Inspection'

    def get_reference_material(self):
        return TMMDEInstance.objects.get(id=self.material_instance.id)


# Pipework related inspections
class AbstractPipeworkInspection(Inspection):
    material_instance = models.ForeignKey('core.PipeworkInstance', on_delete=models.CASCADE, null=True)
    class Meta:
        abstract = True

    def get_reference_material(self):
        return PipeworkInstance.objects.get(id=self.material_instance.id)


class PipeworkNDEInspection(AbstractPipeworkInspection):
    class Meta:
        verbose_name = 'Pipework NDE Inspection'

class PrePostJobInspection(AbstractPipeworkInspection):
    class Meta:
        verbose_name = 'Pipework Pre-Post Inspection'

class AnnualInspection(AbstractPipeworkInspection):
    class Meta:
        verbose_name = 'Pipework Annual Maintenance'

class MajorInspection(AbstractPipeworkInspection):
    class Meta:
        verbose_name = 'Pipework COC Maintenance'
from django.db import models
from core.models import Instance
import datetime
import uuid

WARNING_WINDOW_WEEKS = 6

# Create your models here.
# Inspections tied to an Instance:
class Inspection(models.Model):
    id = models.UUIDField('ID',default=uuid.uuid4,primary_key=True,unique=True,help_text="Unique ID for Material Instance")
    validity_start_date = models.DateField('Start Date',null=True)
    validity_end_date = models.DateField('Expiry Date',null=True)
    material_instance = models.ForeignKey('core.Instance',on_delete=models.CASCADE,null=True, verbose_name="Instance S/N")
    validity = models.BooleanField('Inspection Valid', default=True, help_text="Is the inspection valid?")
    in_use = models.BooleanField('Inspection In Use', default=True, help_text="Is the inspection in use?")

    LIFTING_MATL_TYPE = {
        ('k' , 'Skid'),
        ('s' , 'Sling'),
    }

    class Meta():
        abstract = True
        verbose_name = "Inspection"

    def __str__(self):
        return f'{self.id}'

    def get_reference_material(self):
        return Instance.objects.get(id=self.material_instance.id)

    def checkexpiry(self):
        instance = self.get_reference_material()
        if(self.validity_end_date < datetime.date.today()):
            self.validity = False
            self.save()
            instance.set_expire()
        elif(self.validity_end_date <= (datetime.date.today() + datetime.timedelta(weeks=WARNING_WINDOW_WEEKS))):
            instance.set_warning()

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
class LiftingInspection(Inspection):
    type = models.CharField(
        max_length = 1,
        choices = Inspection.LIFTING_MATL_TYPE,
        default = 'k',
        help_text = "Type of Item"
    )
    class Meta:
        abstract = True

class VisualInspection(LiftingInspection):

    class Meta:
        verbose_name_plural = "Lifting Visual Inspections"
        verbose_name = "Visual Inspection (Lifting)"

class MPIInpection(LiftingInspection):

    class Meta:
        verbose_name_plural = "Lifting MPI Inspections"
        verbose_name = "MPI Inspection (Lifting)"


# Measuring and Monitoring equipment inspections
class CalibrationInspection(Inspection):
    class Meta:
        verbose_name = 'Calibration Inspection'


# Pipework related inspections
class PipeworkNDEInspection(Inspection):
    class Meta:
        verbose_name = 'Pipework NDE Inspection'

class PrePostJobInspection(Inspection):
    class Meta:
        verbose_name = 'Pipework Pre-Post Inspection'

class AnnualInspection(Inspection):
    class Meta:
        verbose_name = 'Pipework Annual Maintenance'

class MajorInspection(Inspection):
    class Meta:
        verbose_name = 'Pipework COC Maintenance'
from django.db import models
import datetime
import uuid

WARNING_WINDOW_WEEKS = 6

# Create your models here.
class Material(models.Model):
    hal_number = models.IntegerField('HAL SAP Number',primary_key=True,unique=True,help_text="SAP Number used by Halliburton Internal")
    hal_description = models.CharField('Description',max_length=255, help_text="Description of Material")
    hal_old_number = models.CharField('HAL Old Mtl Number',max_length=64, help_text="Old Material number used by Halliburton Internal")

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.hal_number} - {self.hal_description}'

# Single Instance of a Material type
class Instance(models.Model):
    id = models.UUIDField('ID',default=uuid.uuid4,primary_key=True,unique=True,help_text="Unique ID for Material Instance")
    material = models.ForeignKey('Material',verbose_name='Material Item', on_delete=models.SET_NULL,null=True)
    serial_number = models.CharField('Mfg S/N',max_length=64,help_text="Manufacturing Serial Number")

    OBJ_STATUS = {
        ('n' , 'Not Ready'),
        ('r' , 'Ready'),
        ('w', 'Expiring'),
        ('e' , 'Expired'),
    }

    status = models.CharField(
        max_length = 1,
        choices = OBJ_STATUS,
        default = 'n',
        help_text = "Status of Item"
    )

    instance_allocation = models.ForeignKey(
        'JobLocation',
        on_delete=models.SET_NULL,
        help_text = "Item Allocated to which project",
        null=True
    )

    instance_remarks = models.CharField('Additional Remarks',max_length=255,help_text="Additional Comments",null=True, blank=True)

    def __str__(self):
        return f'{self.serial_number} - {self.material.hal_description}'

    def set_expire(self):
        self.status = 'e'
        self.save()

    def set_warning(self):
        self.status = 'w'
        self.save()

    def set_notready(self):
        self.status = 'n'
        self.save()

# Certificate tied to an Instance:
class NDECertificate(models.Model):
    id = models.UUIDField('ID',default=uuid.uuid4,primary_key=True,unique=True,help_text="Unique ID for Material Instance")
    certificate_number = models.CharField('Cert. Number',max_length=255, help_text="Certificate Number")
    validity_start_date = models.DateField('Start Date',null=True)
    validity_end_date = models.DateField('Expiry Date',null=True)
    material_instance = models.ForeignKey('Instance',on_delete=models.CASCADE,null=True, verbose_name="Instance S/N")
    validity = models.BooleanField('Certificate Valid', default=True, help_text="Is the certificate valid?")
    in_use = models.BooleanField('Certificate In Use', default=True, help_text="Is the certificate in use?")

    class Meta():
        verbose_name = "NDE Certificate"
        verbose_name_plural = "NDE Certificates"

    def __str__(self):
        return f'{self.certificate_number}'

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

# Location Instance
class JobLocation(models.Model):
    id = models.UUIDField('ID',default=uuid.uuid4,primary_key=True,unique=True,help_text="Unique ID for Location")
    location_name = models.CharField('Location Name',max_length=64,help_text="Name of Location")

    class Meta():
        verbose_name_plural = "Job Locations"

    def __str__(self):
        return f'{self.location_name}'

from django.db import models
import datetime
import uuid

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
        ('e' , 'Expired')
    }

    ALLOCATION = {
        ('w' , 'West Pumping'),
        ('p', 'Plug & Abandonment'),
        ('h', 'Hydraulic WorkOver')
    }

    status = models.CharField(
        max_length = 1,
        choices = OBJ_STATUS,
        default = 'n',
        help_text = "Status of Item"
    )

    instance_allocation = models.CharField(
        max_length = 1,
        choices = ALLOCATION,
        help_text = "Item Allocated to which project",
        null=True
    )

    instance_remarks = models.CharField('Additional Remarks',max_length=255,help_text="Additional Comments",null=True,default="")

    def __str__(self):
        return f'{self.material.hal_number} - {self.material.hal_description}'


    def set_expire(self):
        self.status = 'e'
        self.save()

# Certificate tied to an Instance:
class NDECertificate(models.Model):
    id = models.UUIDField('ID',default=uuid.uuid4,primary_key=True,unique=True,help_text="Unique ID for Material Instance")
    certificate_number = models.CharField('Cert. Number',max_length=255, help_text="Certificate Number")
    validity_start_date = models.DateField('Start Date',null=True)
    validity_end_date = models.DateField('Expiry Date',null=True)
    material_instance = models.ForeignKey('Instance',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.certificate_number}'

    def checkexpiry(self):
        if(self.validity_end_date < datetime.date.today()):
            instance = Instance.objects.get(id=self.material_instance.id)
            instance.set_expire()

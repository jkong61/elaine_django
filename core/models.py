from django.db import models
import datetime
import uuid

# Create your models here.
class Material(models.Model):
    hal_number = models.IntegerField('HAL SAP Number',primary_key=True,unique=True,help_text="SAP Number used by Halliburton Internal")
    hal_description = models.CharField('Description',max_length=255, help_text="Description of Material")
    hal_old_number = models.CharField('HAL Old Mtl Number',max_length=64, help_text="Old Material number used by Halliburton Internal")
    material_type = models.ForeignKey('MaterialType',on_delete=models.CASCADE,null=True,verbose_name="Equipment Type")

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
        null=True,
        blank=True
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

    def get_reference_material(self):
        return Material.objects.get(id=self.material.id)

        
# Location Instance
class JobLocation(models.Model):
    location_name = models.CharField('Location Name',max_length=64,help_text="Name of Location")

    class Meta():
        verbose_name_plural = "Job Locations"

    def __str__(self):
        return f'{self.location_name}'


# Material Type
class MaterialType(models.Model):
    description = models.CharField('Description',max_length=64,help_text="Category of Equipment")

    class Meta():
        verbose_name = "Category"
        verbose_name_plural = "Material Categories"

    def __str__(self):
        return f'{self.description}'

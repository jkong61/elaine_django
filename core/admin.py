from django.contrib import admin
from .models import Material, Instance, NDECertificate, JobLocation

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('hal_number', 'hal_description')

@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('material', 'serial_number', 'status', 'instance_allocation')

@admin.register(NDECertificate)
class NDECertAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'validity_start_date', 'validity_end_date', 'material_instance')

@admin.register(JobLocation)
class JobLocationAdmin(admin.ModelAdmin):
    list_display = ['location_name']
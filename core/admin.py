from django.contrib import admin
from .models import Material, Instance, VisualInspection, MPIInpection, CalibrationInspection, JobLocation, MaterialType

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('hal_number', 'hal_description','material_type')

@admin.register(Instance)
class InstanceAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('material', 'serial_number', 'status', 'instance_allocation')

@admin.register(VisualInspection)
class VisualInspectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'material_instance', 'validity', 'in_use')

@admin.register(MPIInpection)
class MPIInpectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'material_instance', 'validity', 'in_use')

@admin.register(CalibrationInspection)
class CalibrationInspectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'material_instance', 'validity', 'in_use')


@admin.register(JobLocation)
class JobLocationAdmin(admin.ModelAdmin):
    list_display = ['location_name']

@admin.register(MaterialType)
class MatlDescAdmin(admin.ModelAdmin):
    list_display = ['description']
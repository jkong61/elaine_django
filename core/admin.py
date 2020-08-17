from django.contrib import admin
from .models import Material, JobLocation, MaterialType
from .models import PipeworkInstance, SkidInstance, SlingInstance, TMMDEInstance

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('hal_number', 'hal_description','material_type')

@admin.register(PipeworkInstance, SkidInstance, SlingInstance, TMMDEInstance)
class InstancesAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('material', 'serial_number', 'status', 'instance_allocation')

@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(JobLocation)
class JobLocationAdmin(admin.ModelAdmin):
    list_display = ['location_name']
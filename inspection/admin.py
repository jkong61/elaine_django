from django.contrib import admin
from .models import VisualInspection, MPIInpection, CalibrationInspection

# Register your models here.
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


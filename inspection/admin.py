from django.contrib import admin

# Ordinary imports
from .models import VisualInspection, MPIInpection, CalibrationInspection

# Pipework related imports
from .models import PipeworkNDEInspection, PrePostJobInspection, AnnualInspection , MajorInspection

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

@admin.register(PipeworkNDEInspection)
class PipeworkNDEInspectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'material_instance', 'validity', 'in_use')

@admin.register(AnnualInspection)
class AnnualInspectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'material_instance', 'validity', 'in_use')

@admin.register(PrePostJobInspection)
class PrePostJobInspectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'material_instance', 'validity', 'in_use')

@admin.register(MajorInspection)
class MajorInspectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'material_instance', 'validity', 'in_use')
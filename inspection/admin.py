from django.contrib import admin

# Ordinary imports
from .models import CalibrationInspection

from .models import SkidVisualInspection, SkidMPIInpection, SlingVisualInspection, SlingMPIInpection

# Pipework related imports
from .models import PipeworkNDEInspection, PrePostJobInspection, AnnualInspection , MajorInspection

# Register your models here.
@admin.register(
    SkidVisualInspection,
    SkidMPIInpection,
    SlingVisualInspection,
    SlingMPIInpection,
    CalibrationInspection,
    PipeworkNDEInspection,
    PrePostJobInspection,
    AnnualInspection,
    MajorInspection)
class InspectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'material_instance','validity', 'in_use')
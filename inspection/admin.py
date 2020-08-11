from django.contrib import admin

# Ordinary imports
from .models import VisualInspection, MPIInpection, CalibrationInspection

# Pipework related imports
from .models import PipeworkNDEInspection, PrePostJobInspection, AnnualInspection , MajorInspection

# Register your models here.
@admin.register(VisualInspection, MPIInpection, CalibrationInspection, PipeworkNDEInspection, PrePostJobInspection, AnnualInspection , MajorInspection)
class InspectionAdmin(admin.ModelAdmin):
    readonly_fields = ['id']
    list_display = ('validity_start_date', 'validity_end_date', 'validity', 'in_use')
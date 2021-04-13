from django.contrib import admin
from .models import Medicine,Patient
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Medicine)
class MedicineAdmin(ImportExportModelAdmin):
    list_display = ('id', 'med_description')
    pass

@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
    list_display = ('lastname', 'firstname', 'dob', 'weight')
    pass
from django.contrib import admin
from .models import MedicineStatic, Patient, Form, Frequency, Route, Student, Prescription, PreToMedLog
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(MedicineStatic)
class MedicineStaticAdmin(ImportExportModelAdmin):
    list_display = ('medName',)
    pass


@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
    list_display = ('lastname', 'firstname', 'dob', 'weight', 'allergen1', 'allergy1')
    pass


@admin.register(Form)
class FormAdmin(ImportExportModelAdmin):
    list_display = ('form',)
    pass


@admin.register(Frequency)
class FrequencyAdmin(ImportExportModelAdmin):
    list_display = ('frequency',)
    pass


@admin.register(Route)
class RouteAdmin(ImportExportModelAdmin):
    list_display = ('route',)
    pass


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('uid',)
    pass


admin.site.register(Prescription)
# admin.site.register(MedicineLog)
admin.site.register(PreToMedLog)

# test
# admin.site.register(MedicineStatic)
# admin.site.register(Patient)
# admin.site.register(Form)
# admin.site.register(Frequency)
# admin.site.register(Route)
# admin.site.register(Student)

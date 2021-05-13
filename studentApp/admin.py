from django.contrib import admin
from .models import MedicineStatic, Patient, Form, Frequency, Route, Student, Prescription, MedicineLog
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(MedicineStatic)
class MedicineStaticAdmin(ImportExportModelAdmin):
    list_display = ('id','medName')
    pass


@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):
    list_display = ('id','lastname', 'firstname', 'dob', 'weight', 'allergen1', 'allergy1')
    pass


@admin.register(Form)
class FormAdmin(ImportExportModelAdmin):
    list_display = ('id','form')
    pass


@admin.register(Frequency)
class FrequencyAdmin(ImportExportModelAdmin):
    list_display = ('id','frequency',)
    pass


@admin.register(Route)
class RouteAdmin(ImportExportModelAdmin):
    list_display = ('id','route')
    pass


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('id','uid')
    pass


@admin.register(Prescription)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('id','patient','student','review')
    pass


# admin.site.register(Prescription)
# admin.site.register(MedicineLog)
admin.site.register(MedicineLog)

# test
# admin.site.register(MedicineStatic)
# admin.site.register(Patient)
# admin.site.register(Form)
# admin.site.register(Frequency)
# admin.site.register(Route)
# admin.site.register(Student)

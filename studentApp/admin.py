from django.contrib import admin
from .models import MedicineStatic, Patient, Form, Frequency, Route, Student, Prescription, MedicineLog,Marker
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
    list_display = ('id','uid','password')
    pass


# def prescription_by_uid(obj):
#     return obj.student.uid


@admin.register(Prescription)
class PrescriptionAdmin(ImportExportModelAdmin):

    def prescription_by_uid(obj):
        return obj.student.uid

    def patientid(obj):
        return obj.patient.id

    def patient_lastname(obj):
        return obj.patient.lastname

    def patient_firstname(obj):
        return obj.patient.firstname

    list_display = ('id', prescription_by_uid, patientid, patient_lastname, patient_firstname,'review')
    prescription_by_uid.admin_order_field = 'student_id'
    patientid.admin_order_field = 'patient_id'
    patient_lastname.admin_order_field = 'patient'



# admin.site.register(Prescription)
# admin.site.register(MedicineLog)
admin.site.register(MedicineLog)
admin.site.register(Marker)

# test
# admin.site.register(MedicineStatic)
# admin.site.register(Patient)
# admin.site.register(Form)
# admin.site.register(Frequency)
# admin.site.register(Route)
# admin.site.register(Student)

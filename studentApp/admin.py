from django.contrib import admin
from .models import Student,Prescription,PresMed,Frequency,Form,Route,Medicine,Patient
from import_export.admin import ImportExportModelAdmin


# Register your models here.


@admin.register(Frequency)
class MedicineAdmin(ImportExportModelAdmin):
    list_display = ('id', 'frequency')
    pass

@admin.register(Form)
class MedicineAdmin(ImportExportModelAdmin):
    list_display = ('id', 'form')
    pass

@admin.register(Route)
class MedicineAdmin(ImportExportModelAdmin):
    list_display = ('id', 'route')
    pass

admin.site.register(Medicine)
admin.site.register(Patient)
admin.site.register(Student)
admin.site.register(Prescription)
admin.site.register(PresMed)



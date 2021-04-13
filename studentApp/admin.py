from django.contrib import admin
from .models import Medicine
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(Medicine)
class MedicineAdmin(ImportExportModelAdmin):
    list_display = ('id', 'med_description')
    pass
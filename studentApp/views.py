from django.shortcuts import render,redirect
from django.http import HttpResponse
from studentApp.resources import MedicineResources
# Create your views here.
def export(request):
    medicine_resource = MedicineResources()
    meds = medicine_resource.export()
    response = HttpResponse(meds.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="meds.csv"'
    #response = HttpResponse(meds.json, content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="medicine.json"'
    return response
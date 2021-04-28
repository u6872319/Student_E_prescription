from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .resources import MedicineStaticResources
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicineStatic, Patient, Form, Frequency, Route, Student, Prescription, MedicineLog
from .serializers import MedicineStaticSerializer,PatientSerializer,FormSerializer,FrequencySerializer,RouteSerializer,StudentSerializer, MedicineLogSerializer,PrescriptionSerializer

# Create your views here.


# def export(request):
#     medicine_resource = MedicineStaticResources()
#     meds = medicine_resource.export()
#     response = HttpResponse(meds.csv, content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="meds.csv"'
#     #response = HttpResponse(meds.json, content_type='application/json')
#     #response['Content-Disposition'] = 'attachment; filename="medicine.json"'
#     return response

# create "GET, POST, UPDATE, DELETE" methods for all urls


@api_view(['GET'])
def patientlist(request):
    """
    offer all patient objects to localhost/patientlist, in json format
    """
    if request.method == 'GET':
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


# Need the primary key for Patient from the front end (for 'Put' method)
@api_view(['GET', 'PUT'])
def patient_unique(request, pk):
    try:
        patient = Patient.objects.get(pk = pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PUT':
        patient.weight = request.PUT['editedweight']
        patient.allergen1 = request.PUT['allergen1']
        patient.allergy1 = request.PUT['allergy1']
        patient.save()
        serializer = PatientSerializer(patient)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def patientlast(request, lastname):
    try:
        patient = Patient.objects.get(lastname = lastname)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)


@api_view(['GET'])
def patientfirst(request, firstname):
    try:
        patient = Patient.objects.get(firstname = firstname)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)


@api_view(['GET'])
def patientlastfirst(request, lastname, firstname):
    try:
        patient = Patient.objects.get(lastname = lastname, firstname = firstname)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)


@api_view(['GET'])
def studentlist(request):
    """
    offer all student objects to localhost/studentlist, in json format
    """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


# Need the primary key for Patient from the front end (for 'Put' method)
@api_view(['GET'])
def student_unique(request, uid):
    try:
        student = Student.objects.get(uid = uid)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)


@api_view(['GET'])
def prescriptionlist(request):
    prescriptions = Prescription.objects.all()
    serializer = PrescriptionSerializer(prescriptions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def prescription_unique(request):
    try:
        prescription = Prescription.objects.create(Patient(pk = request.GET['patientPk']),
                                                  Student(pk = request.GET['uid']))
        prescription.save()
    except Prescription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PrescriptionSerializer(prescription)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def medicineLog_forOnePres(request):

    if request.method == 'GET':
        medicinelogs = MedicineLog(Prescription(pk = request.GET['presid']), many = True)
        serializer = MedicineLogSerializer(medicinelogs, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            medicineLog = MedicineLog.objects.get_or_create(Prescription(pk=request.GET['presid']),
                                                            medEdited=request.GET['medEdited'],
                                                            formDes=request.GET['form'],
                                                            freDes=request.GET['frequency'],
                                                            routeDes=request.GET['route'],
                                                            doseDes=request.GET['dose'])
            medicineLog.save()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MedicineLogSerializer(medicineLog)
        serializer.save()
        pass

    elif request.method == 'DELETE':
        try:
            medicineLog = MedicineLog.objects.get(request.GET['medlogID'])
        except MedicineLog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        medicineLog.delete()
        pass




@api_view(['GET'])
def formlist(request):
    if request.method == 'GET':
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def frequencylist(request):
    if request.method == 'GET':
        frequencies = Frequency.objects.all()
        serializer = FrequencySerializer(frequencies, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def routelist(request):
    if request.method == 'GET':
        routes = Route.objects.all()
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)

from django.shortcuts import render,redirect
#from django.http import HttpResponse
# from .resources import MedicineStaticResources
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MedicineStatic, Patient, Form, Frequency, Route, Student, Prescription, MedicineLog, Marker
from .serializers import MedicineStaticSerializer,PatientSerializer,FormSerializer,FrequencySerializer,RouteSerializer,StudentSerializer, MedicineLogSerializer,PrescriptionSerializer,UserSerializer, MarkerSerializer



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



@api_view(['GET', 'PATCH'])
def patient_unique(request, pk):
    try:
        patient = Patient.objects.get(pk = pk)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        # patient.weight = request.data['weight']
        # patient.allergen1 = request.data['allergen1']
        # patient.allergy1 = request.data['allergy1']
        # patient.save()
        if request.data['weight'] == "":
            serializer = PatientSerializer(patient)
            return Response(serializer.data)

        serializer = PatientSerializer(patient,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def patientlast(request, lastname):
    try:
        patients = Patient.objects.get(lastname = lastname)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def patientfirst(request, firstname):
    try:
        patients = Patient.objects.get(firstname = firstname)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patients)
        return Response(serializer.data)


@api_view(['GET'])
def patientlastfirst(request, lastname, firstname):
    try:
        patients = Patient.objects.get(lastname = lastname, firstname = firstname)
    except Patient.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PatientSerializer(patients,many=True)
        return Response(serializer.data)

# user?????????
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

#GET:?????????????????????prescription instances  PUT:??????'pid'(patient id)??????sid???(student id), ??????????????????????????????????????????
#url: http://127.0.0.1:8000/prescriptionlist/
@api_view(['GET','PUT', 'PATCH'])
def prescriptionlist(request):
    if request.method == 'GET':
        prescriptions = Prescription.objects.all()
        serializer = PrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data)

    if request.method == 'PUT':
        # get a patient instance
        patient = Patient.objects.get(id=request.data['pid'])
        # get a student instance
        student = Student.objects.get(id=request.data['sid'])
        # create a prescription instance
        prescription = Prescription.objects.create(patient=patient, student=student)
        serializer = PrescriptionSerializer(prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'PATCH':
        prescription = Prescription.objects.get(pk=request.data['preid'])
        prescription.review = request.data['review']
        serializer = PrescriptionSerializer(prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


# class TextAPIView(FlatMultipleModelAPIView):
#
#     def post(self, request, *args, **kwargs):
#         querylist = self.get_querylist()
#         return Response(querylist)
#
#     def get_querylist(self):
#         prescription = Prescription.objects.get(pk=self.request.data['preid'])
#         prescription.review = self.request.data['review']
#         medicinelogs = MedicineLog.objects.filter(prescription=prescription)
#         querylist = [
#             {'queryset': prescription, 'serializer_class': PrescriptionSerializer},
#             {'queryset': medicinelogs, 'serializer_class': MedicineLogSerializer},
#         ]
#         return querylist


#GET:????????????id???????????????????????????instance
#url:http://127.0.0.1:8000/prescriptionlist/??????id/
@api_view(['GET'])
def prescription_unique(request,pk):
    if request.method == 'GET':
        prescription = Prescription.objects.get(pk=pk)
        serializer = PrescriptionSerializer(prescription)
        return Response(serializer.data)



#GET:???????????????????????????medicine???????????????????????????
#PUT????????????preid???(??????id)???'medEdited'(??????????????????????????????)??????form???(?????????????????????????????????form)??? ???frequency??????????????????????????????
# ?????????frequency?????? ???route???????????????????????????????????????route?????? ???dose???????????????????????????????????????dose?????????????????????????????????id???????????????
# medicine?????????(????????????????????????add?????????????????????)
#url: http://127.0.0.1:8000/medicineloglist/
@api_view(['GET', 'PUT'])
def medicineloglist(request):
    if request.method == 'GET':
        medicinelogs = MedicineLog.objects.all()
        serializer = MedicineLogSerializer(medicinelogs, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        prescription = Prescription.objects.get(id=request.data['preid'])
        medicinelog = MedicineLog.objects.create(prescription=prescription,
                                                medEdited=request.data['medEdited'],
                                                formDes=request.data['form'],
                                                freDes=request.data['frequency'],
                                                routeDes=request.data['route'],
                                                doseDes=request.data['dose'])
        serializer = MedicineLogSerializer(medicinelog, data=request.data)
        if serializer.is_valid():
            serializer.save()
        medicinelogs = MedicineLog.objects.all().filter(prescription = prescription)
        serializer2 = MedicineLogSerializer(medicinelogs, many=True)
        # if serializer2.is_valid():
        #     serializer.save()
        return Response(serializer2.data)

#GET?????????medicinelog???id??????????????????medicinelog??????????????????????????????
#DELETE?????????medicinelog???id??????????????????medicinelog????????????????????????????????????medicine??????????????????delete??????????????????
#url: http://127.0.0.1:8000/medicineloglist/????????????medicinelog???id
@api_view(['GET','DELETE'])
def medicineLog_forOnePres(request,pk):

    if request.method == 'GET':
        medicinelog = MedicineLog.objects.get(pk = pk)
        serializer = MedicineLogSerializer(medicinelog)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        medicinelog = MedicineLog.objects.get(pk=pk)
        medicinelog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def prebased_medlogs(request):
    if request.method == 'POST':
        prescription = Prescription.objects.get(pk = request.data['preid'])
        medicinelogs = MedicineLog.objects.all().filter(prescription = prescription)
        serilalizer = MedicineLogSerializer(medicinelogs, many=True)
        return Response(serilalizer.data)

@api_view(['POST'])
def studentbasedpres(request):
    if request.method == 'POST':
        student = Student.objects.get(uid = request.data['uid'])
        prescriptions = Prescription.objects.all().filter(student = student).latest()
        serilalizer = PrescriptionSerializer(prescriptions)
        medicinelogs = MedicineLog.objects.all().filter(prescription = prescriptions)
        serilalizer_med = MedicineLogSerializer(medicinelogs, many=True)
        return Response({
            'prescription':serilalizer.data,
            'medicinelogs':serilalizer_med.data
        })


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


@api_view(['GET'])
def medicinestaticlist(request):
    if request.method == 'GET':
        medstatic = MedicineStatic.objects.all()
        serializer = MedicineStaticSerializer(medstatic, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def userlist(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def user_unique(request,username):
    if request.method == 'GET':
        user = User.objects.get(username = username)
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET'])
def markerlist(request):
    if request.method == 'GET':
        markers = Marker.objects.all()
        serializer = MarkerSerializer(markers, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def marker_unique(request,markername):
    if request.method == 'GET':
        marker = Marker.objects.get(markername = markername)
        serializer = MarkerSerializer(marker)
        return Response(serializer.data)




def login(request):
    return render(request, 'login.html')

def Assessorlogin(request):
    return render(request, 'Assessorlogin.html')


def patientConfirm(request):
    return render(request, 'patientConfirm.html')


def patientSelect(request):
    return render(request, 'patientSelect.html')


def prescription(request):
    return render(request, 'prescription.html')

def detail(request):
    return render(request, 'detail.html')

def Assessor(request):
    return render(request, 'Assessor.html')

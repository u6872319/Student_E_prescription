from django.shortcuts import render,redirect
from django.http import HttpResponse
# from .resources import MedicineStaticResources
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MedicineStatic, Patient, Form, Frequency, Route, Student, Prescription, MedicineLog
from .serializers import MedicineStaticSerializer,PatientSerializer,FormSerializer,FrequencySerializer,RouteSerializer,StudentSerializer, MedicineLogSerializer,PrescriptionSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_multiple_model.views import FlatMultipleModelAPIView
from rest_framework.permissions import AllowAny


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

# user的变量
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

#GET:获得所有现存的prescription instances  PUT:给我'pid'(patient id)和‘sid’(student id), 返回一个新建的药方的所有字段
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


#GET:根据药方id获得一个指定的药方instance
#url:http://127.0.0.1:8000/prescriptionlist/药方id/
@api_view(['GET'])
def prescription_unique(request,pk):
    if request.method == 'GET':
        prescription = Prescription.objects.get(pk=pk)
        serializer = PrescriptionSerializer(prescription)
        return Response(serializer.data)



#GET:获得所有学生填写的medicine条目（应该没啥用）
#PUT：给我‘preid’(药方id)，'medEdited'(学生填写的一个药品名)，‘form’(学生填写的药品名对应的form)， ‘frequency’（学生填写的药品名
# 对应的frequency）， ‘route’（学生填写的药品名对应的route）， ‘dose’（学生填写的药品名对应的dose），给你返回跟这个药方id绑定的所有
# medicine的字段(每条药品写完按下add键触发，或学生)
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

#GET：根据medicinelog的id获得一条对应medicinelog的信息（应该没啥用）
#DELETE：根据medicinelog的id删除一条对应medicinelog的信息（学生删除自己写的medicine条目时，点击delete按键时触发）
#url: http://127.0.0.1:8000/medicineloglist/对应一条medicinelog的id
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




def login(request):
    return render(request, 'login.html')


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

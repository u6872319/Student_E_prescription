from rest_framework import serializers
from .models import Patient, Form, Frequency, Route, Student, MedicineLog, MedicineStatic, Prescription,Marker
from django.contrib.auth.models import User


class MedicineStaticSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineStatic
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class FrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequency
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class MedicineLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineLog
        fields = '__all__'
        depth = 4

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
        depth = 2
    # def create(self, validated_data):
    #     # get a patient instance
    #     patient = Patient.objects.get(id=validated_data['pid'])
    #     # get a student instance
    #     student = Student.objects.get(id=validated_data['sid'])
    #     # create a prescription instance
    #     prescription = Prescription.objects.create(patient=patient, student=student)
    #     prescription.save()
    #     return prescription


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MarkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marker
        field = '__all__'
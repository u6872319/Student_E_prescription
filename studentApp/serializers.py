from rest_framework import serializers
from .models import Patient, Form, Frequency, Route, Student, MedicineLog, MedicineStatic, Prescription

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

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
        depth = 1
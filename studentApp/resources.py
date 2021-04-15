from import_export import resources
from .models import MedicineStatic, Patient, Form, Frequency, Route, Student


class MedicineStaticResources(resources.ModelResource):
    class Meta:
        model = MedicineStatic


class PatientResources(resources.ModelResource):
    class Meta:
        model = Patient


class FormResources(resources.ModelResource):
    class Meta:
        model = Form


class FrequencyResources(resources.ModelResource):
    class Meta:
        model = Frequency


class RouteResources(resources.ModelResource):
    class Meta:
        model = Route


class StudentResources(resources.ModelResource):
    class Meta:
        model = Student

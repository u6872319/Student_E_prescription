from import_export import resources
from .models import MedicineStatic, Patient, Form, Frequency, Route, Student


class MedicineStaticResources(resources.ModelResource):
    class Meta:
        model = MedicineStatic
        import_id_fields = ['medName']
        export_order = ('medName',)
        exclude = ('id',)

class PatientResources(resources.ModelResource):
    class Meta:
        model = Patient
        import_id_fields = ['id']


class FormResources(resources.ModelResource):
    class Meta:
        model = Form
        import_id_fields = ['form']
        export_order = ('form',)
        exclude = ('id',)

class FrequencyResources(resources.ModelResource):
    class Meta:
        model = Frequency
        import_id_fields = ['frequency']
        export_order = ('frequency',)
        exclude = ('id',)

class RouteResources(resources.ModelResource):
    class Meta:
        model = Route
        import_id_fields = ['route']
        export_order = ('route',)
        exclude = ('id',)

class StudentResources(resources.ModelResource):
    class Meta:
        model = Student
        import_id_fields = ['uid']
        export_order = ('uid',)
        exclude = ('id',)

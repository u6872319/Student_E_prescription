from import_export import resources
from studentApp.models import Medicine,Patient

class MedicineResources(resources.ModelResource):
    class Meta:
        model = Medicine

class PatientResources(resources.ModelResource):
    class Meta:
        model = Patient
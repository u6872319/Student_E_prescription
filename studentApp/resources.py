from import_export import resources
from studentApp.models import Medicine

class MedicineResources(resources.ModelResource):
    class Meta:
        model = Medicine
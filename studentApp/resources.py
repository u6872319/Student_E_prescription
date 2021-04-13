from import_export import resources
from studentApp.models import Form,Frequency,Route

class FormResources(resources.ModelResource):
    class Meta:
        model = Form

class FrequencyResources(resources.ModelResource):
    class Meta:
        model = Frequency

class RouteResources(resources.ModelResource):
    class Meta:
        model = Route




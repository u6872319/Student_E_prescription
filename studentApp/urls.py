from . import views
from django.conf.urls import url
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^patientlist/$', views.patientlist),
    url(r'^patientlist/(?P<pk>[0-9]+)$', views.patient_unique),
    url(r'^studentlist/$', views.studentlist),
    url(r'^studentlist/(?P<uid>[a-zA-Z0-9]+)$', views.student_unique),
    url(r'^prescriptionlist/$', views.prescription_unique),
    url(r'^prescriptionlist/(?P<pk>[0-9]+)$', views.prescription_unique),
    url(r'^formlist/$', views.formlist),
    url(r'^frequencylist/$', views.frequencylist),
    url(r'^routelist/$', views.routelist),
    url(r'^medicineLoglist/$', views.medicineLog_forOnePres),
    url(r'^patientlist/(?P<lastname>[a-zA-Z]+)$', views.patientlast),
    url(r'^patientlist/(?P<firstname>[a-zA-Z]+)$', views.patientfirst),
    url(r'^patientlist/(?P<lastname>[a-zA-Z]+)/(?P<firstname>[a-zA-Z]+)$', views.patientlastfirst),
]
urlpatterns = format_suffix_patterns(urlpatterns)
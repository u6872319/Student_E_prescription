"""Student_E_prescription URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from studentApp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    #path('', views.index),
    #url(r'^export-csv/$', views.export, name='export')
    url(r'^', include('studentApp.urls')),
    path('', lambda request: HttpResponse('the cow jumped over the moon')),
    # path('admin/', admin.site.urls),
    path('login/', views.login),
    path('Assessorlogin/', views.Assessorlogin),
    path('patientConfirm/', views.patientConfirm, name="patientConfirm"),
    path('patientSelect/', views.patientSelect, name="patientSelect"),
    path('prescription/', views.prescription, name="prescription"),
    path('detail/', views.detail, name="detail"),
    path('Assessor/', views.Assessor, name="Assessor"),
]

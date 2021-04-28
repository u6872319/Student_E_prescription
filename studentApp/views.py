from django.shortcuts import render


def login(request):

    return render(request, 'login.html')

def patientConfirm(request):

    return render(request, 'patientConfirm.html')

def patientSelect(request):

    return render(request, 'patientSelect.html')
# Create your views here.

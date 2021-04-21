from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from . import  Post_method
def index(request):
    return render(request, 'x.html')


def y_(request):
    data = ["asdasdasdasdasdasdasdasdasd"]
    return render(request, 'y.html')

# Create your views here.
def show(request):
    s=Post_method

    data = {
        "ssssssxss"
    }
    return render(request, 'y.html',locals())

def domain_list(request):
    data = [1,2,3,4,5,6]
    return render(request, 'y.html', locals())




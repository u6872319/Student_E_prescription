from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse

# 接收POST请求数据
import json
def search_post(request):
    data={
        'patient_name': 'apple',
        'age': '25',
        'patient_id': '19000347',
    }
    if request.POST:
        m= request.POST['q']
    return HttpResponse("Post_method.py" + str(m))
    # return HttpResponse(str(json.dump(data)))
def Post_json(Get_value):

    data={
        'patient_name': 'jet',
        'age': '25',
        'patient_id': '19000347',
    }
    if Get_value.POST:
        m= Get_value.POST['json_method']

    # return HttpResponse("Post_method.py" + str(data))

    return HttpResponse(json.dumps('{'+m+":"+'}'), content_type='application/json') # json data
    return json.dumps('{'+m+":"+'}')


def runoob(request):
    return HttpResponse("Hello world 1111")
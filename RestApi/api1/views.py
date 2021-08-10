from django.shortcuts import render
from .serializers import EmployeeDetailsSerializer
from .models import EmployeeDetails
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer

# Create your views here.

def serializer_views(request):
    data1 = EmployeeDetails.objects.all()
    print(data1)
    serialized_data = EmployeeDetailsSerializer(data1,many=True)
    print(serialized_data)
    print(serialized_data.data)
    #json_data = JSONRenderer().render(serialized_data.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serialized_data.data, safe=False)

def serializer_single_views(request,pk):
    data1 = EmployeeDetails.objects.get(id=pk)
    print(data1)
    serialized_data = EmployeeDetailsSerializer(data1)
    print(serialized_data)
    print(serialized_data.data)
    #json_data = JSONRenderer().render(serialized_data.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serialized_data.data, safe=False)
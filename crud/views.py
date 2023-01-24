from django.shortcuts import render

# Create your views here.

from .models import Employee, Request, Stage
from .serializers import EmployeeSerializer
from .serializers import RequestSerializer
from .serializers import StageSerializer

from rest_framework import viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

# В функции index() 
def index(request):
    return render(request, "index.html")

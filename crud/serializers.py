#serializers.py
from rest_framework import serializers
from .models import Employee, Request, Stage

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "login", "password", "name", "email", "admin", "manager")

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("id", "dater", "customer", "address", "phone", "problem", "cost")

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ("id", "request", "dates", "details", "employee")

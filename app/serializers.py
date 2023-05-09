from .models import *
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'post', 'salary']
        
        
class StudentSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
        
        
class StudentRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    
    def create(self, validate_data):
        user = Student(username=validate_data['username'])
        user.set_password(validate_data['password'])
        user.save()
        return user
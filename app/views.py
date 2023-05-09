from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework.decorators import  authentication_classes


class GetEmployee(APIView):
    permission_classes=[IsAuthenticated]
    # authentication_classes=[SessionAuthentication]
    # authentication_classes=[BasicAuthentication]
    @authentication_classes((TokenAuthentication,))
    def get(self, request):
        stu = Employee.objects.all()
        serializer = EmployeeSerializer(stu, many=True)
        return Response({
            'message':'Your Data is here',
            'data':serializer.data,
            'status':status.HTTP_200_OK
        })
        
        
class LoginApi(APIView):
    def post(self, request, formate=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.data.get('username')
            password=serializer.data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({
                    'message':'Login Successfully',
                    'data':serializer.data,
                    'token':str(token),
                    'status':status.HTTP_200_OK
                    })
        return Response({
                'msg':"something went wrong",
                "error":serializer.errors,

            })    
        
        
class RegisterApi(APIView):
    def post(self, request, format=None):
        serializer = StudentRegSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,created = Token.objects.get_or_create(user=user)
            if user is not None:
                return Response({
                    'message':'Register Successfully',
                    'data':serializer.data,
                    'token':str(token),
                    'status':status.HTTP_200_OK
                    })
        return Response({
                'msg':"something went wrong",
                "error":serializer.errors,

            })
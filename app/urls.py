from django.urls import path
from .views import *
urlpatterns = [
    path('GetEmployee/', GetEmployee.as_view()),
    path('LoginApi/', LoginApi.as_view()),
    path('RegisterApi/', RegisterApi.as_view())
]

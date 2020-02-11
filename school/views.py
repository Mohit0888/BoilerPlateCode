from django.shortcuts import render
from .models import Student 
from .serializer import StudentSerializer      
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import mixins
import io
# Create your views here.


class StudentView(generics.GenericAPIView , 
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
        
    def get(self,request,pk=None):
        if pk:
           return self.retrieve(request,pk) 
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,pk=None):
        return self.update(request,pk)

















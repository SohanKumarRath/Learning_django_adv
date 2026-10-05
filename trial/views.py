from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from trial.serializers import StudentSerializer
from .models import Student
# APIView is a low-level DRF class-based view. You explicitly write the logic for each HTTP method.
class StudentApi(APIView):
    def get(self,req):
        students=Student.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    def post(self,req):
        serializer=StudentSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
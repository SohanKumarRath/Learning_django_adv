from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from trial.serializers import StudentSerializer
from .models import Student
# APIView is a low-level DRF class-based view. You explicitly write the logic for each HTTP method.
class StudentApi(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                student = Student.objects.get(stud_id=pk)
            except Student.DoesNotExist:
                return Response(
                    {"error": "Student not found"},
                    status=404
                )

            serializer = StudentSerializer(student)
            return Response(serializer.data)

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        try:
            student = Student.objects.get(stud_id=pk)
        except Student.DoesNotExist:
            return Response(
                {"error": "Student not found"},
                status=404
            )

        serializer = StudentSerializer(
            student,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        try:
            student = Student.objects.get(stud_id=pk)
        except Student.DoesNotExist:
            return Response(
                {"error": "Student not found"},
                status=404
            )

        student.delete()

        return Response(
            {"message": "Student deleted successfully"},
            status=204
        )
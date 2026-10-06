from django.urls import path
from .views import StudentApi
urlpatterns = [
    path('students/', StudentApi.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentApi.as_view(), name='student-detail'),
]
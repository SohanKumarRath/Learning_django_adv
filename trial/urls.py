from django.urls import path
from .views import StudentApi
urlpatterns = [
    path('students/', StudentApi.as_view(), name='student-list'),
]
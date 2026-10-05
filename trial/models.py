from django.db import models

# Create your models here.
class Student(models.Model):
    stud_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField(unique=True,blank=False,null=False)
    phone=models.BigIntegerField(unique=True,blank=False,null=False)
    class Meta:
        db_table='student'

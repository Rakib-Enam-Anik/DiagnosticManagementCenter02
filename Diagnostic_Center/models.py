from django.db import models
from django.contrib.auth.models import User 

# Create your models here.



class Doctor(models.Model):
    name = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null = True)
    specialization = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name
    
class Technician(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    dep = models.CharField(max_length=50)
  
    
    def __str__(self):
        return self.name
    
class Nurse(models.Model):
    name =  models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField(null=True)
    dep = models.CharField(max_length=50)
  
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    mobile = models.IntegerField(null=True)
    date1 = models.DateField()
    time1 = models.TimeField()
    
    def __str__(self):
        return self.doctor.name + "--" + self.patient.name


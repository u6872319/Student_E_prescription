from django.db import models

# Create your models here.
# sql table: Medicine
class Medicine(models.Model):
    med_description = models.CharField(max_length=1000)

# sql table: Patient (dob default format : xxxx-xx-xx)
class Patient(models.Model):
    lastname = models.CharField(max_length=1000)
    firstname = models.CharField(max_length=1000)
    dob = models.DateField()
    weight = models.CharField(max_length=1000)
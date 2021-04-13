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


# sql table: Student
class Student(models.Model):
    uid = models.CharField(max_length=1000)


# sql table: prescription
class Prescription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    edited_weight = models.CharField(max_length=1000)
    edited_allergy1 = models.CharField(max_length=1000)
    edited_allergy2 = models.CharField(max_length=1000)
    edited_allergy3 = models.CharField(max_length=1000)
    edited_allergy4 = models.CharField(max_length=1000)
    edited_allergy5 = models.CharField(max_length=1000)


# sql table for prescription - medicine records
class PresMed(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicineName = models.CharField(max_length=1000)
    doseFreeText = models.CharField(max_length=1000)
    form = models.CharField(max_length=1000)
    route = models.CharField(max_length=1000)
    frequency = models.CharField(max_length=1000)


class Frequency(models.Model):
    frequency = models.CharField(max_length=1000)


class Form(models.Model):
    form = models.CharField(max_length=1000)


class Route(models.Model):
    route = models.CharField(max_length=1000)

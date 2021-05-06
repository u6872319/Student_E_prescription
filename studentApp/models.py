from django.db import models

# Create your models here.


# sql table: Medicine
# class MedicineStatic(models.Model):
#     medName = models.CharField(primary_key=True, max_length=1000)


# sql table: Patient (dob default format : xxxx-xx-xx)
class Patient(models.Model):
    # id = models.AutoField(primary_key=True, max_length=1000)
    lastname = models.CharField(max_length=1000)
    firstname = models.CharField(max_length=1000)
    dob = models.DateField()
    weight = models.CharField(max_length=1000)
    allergen1 = models.CharField(blank=True, max_length=1000)
    allergy1 = models.CharField(blank=True, max_length=1000)


class Form(models.Model):
    form = models.CharField(max_length=1000, blank=True)


class Frequency(models.Model):
    frequency = models.CharField(max_length=1000)


class Route(models.Model):
    route = models.CharField(max_length=1000)


class Student(models.Model):
    uid = models.CharField(max_length=1000)


class Prescription(models.Model):
    #id = models.AutoField(primary_key=True, blank=True)
    patient = models.ForeignKey(to=Patient, on_delete=models.PROTECT, blank=True)
    student = models.ForeignKey(to=Student, on_delete=models.PROTECT, blank=True)
    review = models.TextField(blank=True)


class MedicineStatic(models.Model):
    medName = models.CharField(max_length=1000)


class MedicineLog(models.Model):
    prescription = models.ForeignKey(to=Prescription, on_delete=models.PROTECT)
    medEdited = models.CharField(max_length=1000,blank=True)
    formDes = models.CharField(max_length=1000,blank=True)
    freDes = models.CharField(max_length=1000,blank=True)
    routeDes = models.CharField(max_length=1000,blank=True)
    doseDes = models.CharField(max_length=1000,blank=True)

# class PreToMedLog(models.Model):
#     medStatic = models.ForeignKey(MedicineStatic, on_delete=models.CASCADE)
#     prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
#     formDes = models.CharField(max_length=1000)
#     freDes = models.CharField(max_length=1000)
#     routeDes = models.CharField(max_length=1000)
#     doseDes = models.CharField(max_length=1000)




from django.db import models

# Create your models here.
class Medicine(models.Model):
    med_description = models.CharField(max_length=1000)
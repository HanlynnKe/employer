from django.db import models


# Create your models here.
class WorkerInfo(models.Model):
    workerID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    birth = models.DateField()
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=50)

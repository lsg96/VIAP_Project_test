from django.db import models

# Create your models here.
class CenterInfo(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)

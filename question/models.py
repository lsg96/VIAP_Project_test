from datetime import datetime

from django.db import models

# Create your models here.

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    qname = models.CharField(max_length=16)
    qphone = models.CharField(max_length=16)
    qemail = models.CharField(max_length=40)
    qselect = models.CharField(max_length=20)
    qsubject = models.TextField()
    context = models.TextField()
    regdate = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'qu  estion'

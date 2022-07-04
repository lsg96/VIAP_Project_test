from datetime import datetime

from django.db import models

# Create your models here.


class Zipcode(models.Model):
    ZIPCODE = models.CharField(max_length=7)
    SIDO = models.CharField(max_length=7)
    GUGUN = models.CharField(max_length=30, null=True)
    DONG = models.CharField(max_length=50)
    RI = models.CharField(max_length=100,null=True)
    BUNGI = models.CharField(max_length=40,null=True)
    seq = models.IntegerField(primary_key=True)


    class Meta:
        db_table = 'zipcode'


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=18,unique=True)
    passwd = models.CharField(max_length=18)
    name = models.CharField(max_length=7)
    phone = models.CharField(max_length=15)
    email = models.TextField()
    mailing = models.BooleanField(default=False)
    zip = models.ForeignKey(Zipcode, on_delete=models.DO_NOTHING)
    addr =models.TextField()
    regdate=models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'member'





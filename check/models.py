from datetime import datetime

from django.db import models

# Create your models here.
class CenterInfo(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length=50,null=True)
    addr = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)

    class Meta:
        db_table = 'centerinfo'
        ordering = ['-id']

class Agent(models.Model):
    agid = models.AutoField(primary_key=True)
    agentno = models.CharField(max_length=6)
    sido = models.CharField(max_length=2)
    gugun = models.CharField(max_length=4)
    ro = models.CharField(max_length=10)
    agentname = models.CharField(max_length=5)

    class Meta:
        db_table = 'agent'

class Apply(models.Model):
    appid = models.AutoField(primary_key=True)
    appno = models.CharField(max_length=11)
    pdate = models.CharField(null=False, max_length=10)
    fdate = models.CharField(null=False, max_length=10)
    edate = models.CharField(null=False, max_length=10)
    ptime = models.CharField(max_length=5)
    insptype = models.CharField(max_length=4,default='')
    msg = models.TextField(null=True)
    fnames = models.CharField(max_length=255,null=True)
    agid = models.ForeignKey(Agent, on_delete=models.DO_NOTHING,default=0)

    class Meta:
        db_table = 'apply'
        ordering = ['-appid']

class ApplyUser(models.Model):
    ausrid = models.AutoField(primary_key=True)
    carno = models.CharField(max_length=9)
    appname = models.CharField(max_length=10,null=False)
    carname = models.CharField(max_length=10)
    apptel = models.CharField(max_length=10,null=False)
    alttel = models.CharField(max_length=10)
    birth = models.CharField(max_length=10)
    addr1 = models.CharField(max_length=30)
    addr2 = models.CharField(max_length=30)
    appid = models.ForeignKey(Apply, on_delete=models.DO_NOTHING,default=0)

    class Meta:
        db_table = 'applyuser'

class InspFee(models.Model):
     insptype = models.CharField(max_length=4)
     carsize = models.CharField(max_length=2)
     carname = models.CharField(max_length=10)
     fee = models.CharField(max_length=6, null=True)

     class Meta:
         db_table = 'inspfee'

class Alert(models.Model):
    atid = models.AutoField(primary_key=True)
    atno = models.CharField(max_length=12)
    atname = models.CharField(max_length=10, null=False)
    attel = models.CharField(max_length=10)
    atfdate = models.CharField(null=False, max_length=10)
    atedate = models.CharField(null=False, max_length=10)


    class Meta:
        db_table = 'alert'
        ordering = ['-atid']

class Carzipcode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sido = models.CharField(max_length=20)
    gugun = models.CharField(max_length=20)
    addr = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)

    class Meta:
        db_table = 'carzipcode'
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

class Apply(models.Model):
    appno = models.CharField(primary_key=True,max_length=11)
    pdate = models.DateField(null=False)
    ptime = models.TimeField(null=False)
    agent = models.CharField(max_length=10)
    msg = models.TextField(null=True)
    fnames = models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'apply'
        ordering = ['-appno']

class ApplyUser(models.Model):
    carno = models.CharField(primary_key=True,max_length=9)
    appname = models.CharField(max_length=10,null=False)
    carname = models.CharField(max_length=10)
    apptel = models.CharField(max_length=10,null=False)
    alttel = models.CharField(max_length=10)
    birth = models.CharField(max_length=10)
    addr1 = models.CharField(max_length=10)
    addr2 = models.CharField(max_length=10)
    usrappno = models.ForeignKey(Apply, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'applyuser'

class InspFee(models.Model):
     insptype = models.CharField(max_length=4)
     carsize = models.CharField(max_length=2)
     carname = models.CharField(max_length=10)
     fee = models.CharField(max_length=6, null=True)

     class Meta:
         db_table = 'inspfee'


class Agent(models.Model):
    sido = models.CharField(max_length=2)
    gugun = models.CharField(max_length=4)
    ro = models.CharField(max_length=10)
    agentname = models.CharField(max_length=5)

    class Meta:
        db_table = 'agent'



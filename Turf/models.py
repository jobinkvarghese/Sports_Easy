from django.db import models

# Create your models here.
class turf_reg_tbl(models.Model):
    tname=models.CharField(max_length=50)
    timg=models.FileField(upload_to="pictures")
    tdetails=models.TextField()
    tloc=models.URLField(max_length=200)
    taddress=models.TextField()
    dist=models.CharField(max_length=25)
    temail=models.EmailField(max_length=50)
    tmob=models.CharField(max_length=20)
    ps1=models.CharField(max_length=25)
    ps2=models.CharField(max_length=25)
    Approve=models.BooleanField(default=False)
    status=models.CharField(max_length=100,default="nill")
class slot_tbl(models.Model):
    turf=models.ForeignKey(turf_reg_tbl,on_delete=models.CASCADE)
    stime=models.TimeField()
    etime=models.TimeField()
    amount=models.IntegerField()
    status=models.CharField(max_length=50,default="no issue")


     



     
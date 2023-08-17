from django.db import models

# Create your models here.
class Academy_reg_tbl(models.Model):
    Aname=models.CharField(max_length=100)
    Aimg=models.FileField(upload_to="pictures")
    Adetails=models.TextField()
    dist=models.CharField(max_length=50)
    Address=models.TextField()
    Aloc=models.URLField(max_length=200)
    status=models.CharField(max_length=50,default="seat available")
    Aemail=models.EmailField(unique=True)
    Amob=models.IntegerField()
    Approve=models.BooleanField(default=False)
    password=models.CharField(max_length=12)
    cpass=models.CharField(max_length=12)
    Approved=models.BooleanField(default=False)



from django.db import models

# Create your models here.
class reg_tbl(models.Model):
    fname=models.CharField(max_length=25)
    Lname=models.CharField(max_length=25)
    Age=models.CharField(max_length=3)
    mobile=models.IntegerField()
    Address=models.CharField(max_length=60)
    Gender=models.CharField(max_length=20)
    Email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    
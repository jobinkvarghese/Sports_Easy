from django.db import models
from datetime import datetime


# Create your models here.
class Event_manager_tbl(models.Model):
    emname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile=models.IntegerField()
    Address=models.TextField()
    pass1=models.CharField(max_length=25)
    pass2=models.CharField(max_length=25)
    Approve=models.BooleanField(default=False)
class Event_reg_tbl(models.Model):
    ename=models.CharField(max_length=100)
    em=models.ForeignKey(Event_manager_tbl,on_delete=models.CASCADE)
    eimage=models.FileField(upload_to="pictures")
    eaddress=models.CharField(max_length=100)
    eloc=models.URLField(max_length=200)
    edate=models.DateTimeField()
    eemail=models.EmailField(max_length=100)
    ticket=models.IntegerField()
    mobile=models.IntegerField()
    details=models.CharField(max_length=150)
    ticket_amount=models.IntegerField()
    dist=models.CharField(max_length=25)
    emid=models.IntegerField()
    avl_tickets=models.IntegerField()
    status=models.CharField(max_length=50,default="not change")
    Approve=models.BooleanField(default=True)





    

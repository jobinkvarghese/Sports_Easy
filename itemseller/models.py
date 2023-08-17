from django.db import models

# Create your models here.
class Itemseller_reg_tbl(models.Model):
    sellername=models.CharField(max_length=25)
    Address=models.CharField(max_length=25)
    mobile=models.IntegerField()
    Email=models.EmailField()
    password=models.CharField(max_length=10)
    confirm_password=models.CharField(max_length=10)
    Approve=models.BooleanField(default=False)

    def __str__(self):
        return self.sellername
    
class Pcategory(models.Model):
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname
    
class product_upload_tbl(models.Model):
    catid=models.ForeignKey(Pcategory,on_delete=models.CASCADE)
    sellerid=models.IntegerField()
    sellername=models.CharField(max_length=100)
    seller=models.ForeignKey(Itemseller_reg_tbl,on_delete=models.CASCADE)
    productname=models.CharField(max_length=25)
    productamount=models.IntegerField()
    productdetails=models.CharField(max_length=100)
    productimage=models.FileField(upload_to="pictures")
    status=models.CharField(max_length=25,default="stock available")

    def __str__(self):
        return self.productname

      
    
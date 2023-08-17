from django.db import models
from itemseller . models import product_upload_tbl
from itemseller . models import Itemseller_reg_tbl
from datetime import datetime, timedelta
from Event.models import Event_manager_tbl,Event_reg_tbl
from Academy.models import Academy_reg_tbl
from Turf . models import turf_reg_tbl


# Create your models here.

class User_regtbl(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    mob = models.IntegerField()
    ag = models.IntegerField()
    ad = models.TextField()
    gn = models.CharField(max_length=10)
    eml = models.EmailField(unique=True)
    ps1 = models.CharField(max_length=25)
    ps2 = models.CharField(max_length=25)
class add_to_cart_table(models.Model):
      product = models.ForeignKey(product_upload_tbl, on_delete=models.CASCADE)
      userid = models.IntegerField()
      proid=models.IntegerField()

class Booking(models.Model):
    user=models.ForeignKey(User_regtbl,on_delete=models.SET_DEFAULT,default="this user account is deleted")
    product = models.ForeignKey(product_upload_tbl, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    Amount=models.IntegerField()
    order_date = models.DateTimeField(default=datetime.today())
    arrival_date = models.DateTimeField(default=datetime.today()+timedelta(7))
    status=models.CharField(max_length=15)
    Alt_phone=models.IntegerField()
    shipping_Address=models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.arrival_date:
            order=datetime.today()
            self.arrival_date = order+ timedelta(days=7)
        super(Booking, self).save(*args, **kwargs)
    class Meta:
        ordering = ['order_date']   

class book_event_tbl(models.Model):
    event=models.ForeignKey(Event_reg_tbl, on_delete=models.CASCADE)
    audient=models.ForeignKey(User_regtbl,on_delete=models.SET_DEFAULT,default="this user account is deleted")
    ticketno=models.IntegerField()
    amount=models.IntegerField()
    bookingdate=models.DateTimeField(default=datetime.today())
    status=models.CharField(max_length=15,default="notpaid")
    cancel=models.CharField(max_length=100,default="Nill")
class Academy_admission_tbl(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    mob = models.IntegerField()
    ag = models.IntegerField()
    ad = models.TextField()
    gn = models.CharField(max_length=10)
    eml = models.EmailField()
    date=models.DateTimeField(default=datetime.today())
    academy=models.ForeignKey(Academy_reg_tbl,on_delete=models.CASCADE)
    user=models.ForeignKey(User_regtbl,on_delete=models.CASCADE)
class posts_tbl(models.Model):
    pimg=models.FileField(upload_to="pictures")
    Pcaption=models.TextField(default="nocaption")
    user=models.ForeignKey(User_regtbl,on_delete=models.CASCADE)
    approve=models.CharField(max_length=100,default=False)
class comments_tbl(models.Model):
    user=models.ForeignKey(User_regtbl,on_delete=models.CASCADE)
    post=models.ForeignKey(posts_tbl,on_delete=models.CASCADE)
    comment=models.TextField(default="nocomments")
    approve=models.CharField(max_length=100,default=False)
class turf_booking_tbl(models.Model):
    sid=models.IntegerField()
    user=models.ForeignKey(User_regtbl,on_delete=models.SET_DEFAULT,default="this user account is deleted")
    turf=models.ForeignKey(turf_reg_tbl,on_delete=models.CASCADE)
    tdate=models.DateTimeField(default=datetime.today())
    bdate=models.DateField()
    stime=models.TimeField()
    etime=models.TimeField()
    amount=models.IntegerField()
    status=models.CharField(max_length=25,default="unpaid")



#order tracking
class OrderTrac(models.Model):
    STATUS_CHOICES = (
        ('PLACED', 'Order Placed'),
        ('SHIPPING', 'Shipping'),
        ('DELIVERED', 'Delivered'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PLACED')
    # other fields like customer, product, etc.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    orderid=models.ForeignKey(Booking, on_delete=models.CASCADE)
    userid=models.ForeignKey(User_regtbl,on_delete=models.SET_DEFAULT,default="this user account is deleted")
    
    def __str__(self):
        return f"Order {self.pk} - {self.status}"



class Newcartadd(models.Model):
    createdate=models.DateField(auto_now=True)
    product = models.ForeignKey(product_upload_tbl, on_delete=models.CASCADE)
    userid =models.ForeignKey(User_regtbl, on_delete=models.CASCADE)
    qty=models.IntegerField()
    netprice=models.DecimalField(decimal_places=2,max_digits=99)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.createdate

class Fullpayment(models.Model):
    createdate=models.DateField(auto_now=True)
    paydate=models.DateField(auto_now=False)
    netprice=models.DecimalField(decimal_places=2,max_digits=99)
    userid =models.ForeignKey(User_regtbl, on_delete=models.CASCADE)
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.createdate    
    
class OrderTable(models.Model):
    # Define fields for OrderTable
    order_number = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed

    class Meta:
        db_table = 'order_table'    

class OrderItem(OrderTable):
    # Inherit from OrderTable, making it the child class

    # Additional fields for OrderItem
    product_name = models.ForeignKey(product_upload_tbl, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sellerid=models.ForeignKey(Itemseller_reg_tbl, on_delete=models.CASCADE)
    orderstatus=(
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),
        ('Cancel','Cancel')
    )
    status=models.CharField(max_length=150,choices=orderstatus,default='Pending')
    # Add other fields as needed

    class Meta:
        db_table = 'order_item'         
class Placeoreder(models.Model):
    userid=models.ForeignKey(User_regtbl, on_delete=models.CASCADE)
    
    
    placename=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    houseno=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    trackno=models.CharField(max_length=100)
    netprice=models.CharField(max_length=100)
    orderstatus=(
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),
        ('Cancel','Cancel')
    )
    status=models.CharField(max_length=150,choices=orderstatus,default='Pending')
    created_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    def  __str__(self):
        return '{} - {} '.format(self.id,self.tracking)
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.subject

class complaint_reg_tbl(models.Model):
     book=models.ForeignKey(OrderItem, on_delete=models.CASCADE)
     seller= models.ForeignKey(Itemseller_reg_tbl, on_delete=models.CASCADE)
     complaint=models.TextField()
     cdate=models.DateTimeField(auto_now=True)
     cimage=models.FileField(upload_to="pictures")
     status=models.CharField(max_length=100)   
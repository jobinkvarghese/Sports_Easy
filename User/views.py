from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import User_regtbl,complaint_reg_tbl
from itemseller . models import product_upload_tbl,Pcategory
from . models import add_to_cart_table,Academy_admission_tbl,posts_tbl,OrderTrac
from .models import Booking,Newcartadd,Fullpayment,Placeoreder,OrderTable,OrderItem
from django . contrib import messages
from datetime import datetime, timedelta,date,time
from django.utils import timezone
from itemseller . models import Itemseller_reg_tbl
from Event . models import Event_reg_tbl,Event_manager_tbl
from .models import book_event_tbl,comments_tbl,turf_booking_tbl
from Academy.models import Academy_reg_tbl
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from datetime import date
from django.db.models import Sum
import stripe
from django.conf import settings
from .utils import send_custom_email
from .forms import ContactForm
import pytz

from django.core.paginator import Paginator
# Create your views here.

def payment_page(request):
    if request.method == 'POST':
        # Get the amount from the form submission (assuming the form has an input named 'amount')
        amount = request.POST.get('amount')
        
        # Convert amount to cents (Stripe expects the amount in cents)
        amount_in_cents = int(float(amount) * 100)

        # Create a PaymentIntent using the Stripe API
        stripe.api_key = settings.STRIPE_SECRET_KEY
        intent = stripe.PaymentIntent.create(
            amount=amount_in_cents,
            currency='usd',
        )

        return render(request, 'payment_app/checkout.html', {'client_secret': intent.client_secret})

    return render(request, 'payment_app/payment_page.html')
import random

def generate_tracking_number():
    # Generate random numbers for each part of the tracking number
    rand_num1 = str(random.randint(1000, 9999))
    rand_num2 = str(random.randint(1000, 9999))
    rand_num3 = str(random.randint(1000, 9999))

    # Concatenate the random numbers to form the tracking number
    tracking_number = f"TN-{rand_num1}-{rand_num2}-{rand_num3}"
    return tracking_number

def placeorder(req):
    if req.method=="POST":
        trackno=generate_tracking_number()
        usid=req.session['uid']
        userobj=User_regtbl.objects.get(id=usid)
        status=req.POST.get('status')
        sellerid=req.POST.get("itemseller")
        print("status",status)
        cartv=Newcartadd.objects.filter(userid=userobj,status=0)
        tot=0
        if cartv:
            orderno=trackno
            order_table = OrderTable.objects.create(order_number=orderno)
            if order_table:
                order_table.save()
                for ord in cartv:
                    print(ord.product.id)
                    prdobj=product_upload_tbl.objects.get(id=ord.product.id)
                    selobj=Itemseller_reg_tbl.objects.get(id=sellerid)
                    
                    order_item = OrderItem.objects.create(
                        order_number=orderno,
                        product_name=prdobj,
                        quantity=ord.qty,
                        price=ord.netprice,
                        sellerid=selobj

                    )
                    tot=tot+float(ord.netprice)
            
        req.session['orderno']=trackno
        data={
        'userid':userobj,
     
        
     
        'placename':req.POST.get("placename"),
        'city':req.POST.get("city"),
        'state':req.POST.get('state'),
        'country':req.POST.get('country'),
        'landmark':req.POST.get('landmark'),
        'pincode':req.POST.get('pincode'),
        'phone':req.POST.get('phoneNumber'),
        'houseno':req.POST.get('houseno'),
        'netprice':req.POST.get('tprice'),
        'trackno':trackno,
        }
        obj=Placeoreder(**data)
        if obj:
            obj.save()
            return render(req,'payment.html',{'msg':tot})
    return render(req,'payment.html',{'msg':""})
def index(request):

    prd=product_upload_tbl.objects.all().exclude(status='delete')
    items_per_page = 10
    paginator = Paginator(prd, items_per_page)
    page_number = request.GET.get('page')  # Get the page number from the request
    page = paginator.get_page(page_number)
    context = {
    'items': page,
    # Other context data
}
    return render(request,"mainpage/index.html",context)
def User_reg(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('Lname')
        mobile=request.POST.get('mob')
        eml=request.POST.get('email')
        Age=request.POST.get('Age')
        Gen=request.POST.get('Gender')
        Address=request.POST.get('Address')
        pas=request.POST.get('password')
        cpass=request.POST.get('c_password')
        if User_regtbl.objects.filter(eml=eml).exists():
            messages.success(request, 'Another Account Has Similar Email Id')
            return render(request,"user_reg.html")
        else:
          obj=User_regtbl.objects.create( fname=fname,lname=lname,mob=mobile,ag=Age,ad=Address,gn=Gen,eml=eml,ps1=pas,ps2=cpass)
          obj.save()
          if obj:
            return render(request,"User_login.html")
          else:
            return render(request,"user_reg.html")
    else:
        return render(request,"user_reg.html")
def User_login(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        obj=User_regtbl.objects.filter(eml=eml,ps1=psw)
        if obj:
            for l in obj:
                uid=l.id
                request.session['uid']=uid
            return render(request,"User_home.html")
        else:
            messages.success(request,'Login Failed')
            return render(request,"User_login.html")
    else:
        return render(request,"User_login.html")
def sports_items(request):
     mypro=product_upload_tbl.objects.all().exclude(status='delete')
     catid=Pcategory.objects.all()
     return render(request,"newuser_item_view.html",{"view":mypro,"cat":catid}) 
def  add_to_cart(request):
    
    uid=request.session['uid']
    proid=request.POST.get('prdid')
    qty=request.POST.get('qty')
    prc=request.POST.get('netprc')
    prdid=product_upload_tbl.objects.get(id=proid)
    userid=User_regtbl.objects.get(id=uid)
    
    nwobj=Newcartadd.objects.filter(product=prdid,userid=userid,status=0)
  
    mypro=product_upload_tbl.objects.get(id=proid)
    obj1=add_to_cart_table.objects.filter(proid=proid,userid=uid)
    if obj1 and nwobj:
        messages.success(request, 'product already in cart')
        return redirect("/sports_items")
    else:
        obj=add_to_cart_table.objects.create(product=mypro,userid=uid,proid=proid)
        newcrt=Newcartadd.objects.create(product=prdid,userid=userid,qty=qty,netprice=prc,status=0)
        obj.save()
        newcrt.save()
        if obj:
         messages.success(request, 'Item Added to cart')
         return redirect("/sports_items")
        
def cart_view(request):
    uid=request.session['uid']
    usid=User_regtbl.objects.get(id=uid)
    mycart=add_to_cart_table.objects.filter(userid=uid)
    cr_date=date.today();
    d2=cr_date.strftime("%B %d, %Y")
    print(d2)
    nwcrt=Newcartadd.objects.select_related('product','userid').filter(userid=usid,status=0)

    totprice=calculate_sum_with_condition(usid);
    print(totprice)
    if(totprice==None):
        pay=[0,0]
    else:
        pay=[1,1]

    return render(request,"Carted_items.html",{"cart":mycart,'newcart':nwcrt,'netprice':totprice,'pay':pay})

def calculate_sum_with_condition(usid):
    # Assuming 'condition' is a dictionary containing the field and its value to filter the rows
    # For example, {'your_field': 'desired_value'}

    # Use filter() to apply the condition and Sum() to calculate the total
    total_sum =Newcartadd.objects.filter(userid=usid,status=0).aggregate(total=Sum('netprice'))['total']

    # 'total_sum' will now contain the sum of the 'netprice' values based on the given condition
    return total_sum
def userId(idn):
    userid=User_regtbl.objects.get(id=idn)
    return  userid
def newpayment(req):
    if req.method=="POST":
        userid=req.user
        netprice=req.POST.get("ntprice")
        itemsellerid=req.POST.get('itemseller')
        print("itemseller",itemsellerid)
        print(netprice)
        return render(req,'placeorder/placeorder.html',{'nt':netprice,'itemseller':itemsellerid})
    else:
        return redirect("/")
      
def payM(req):
    usid=req.session['uid']
    userobj=User_regtbl.objects.get(id=usid)
    email_id=userobj.eml
    order=req.session['orderno']
    subject = 'Item Purchased'
    message = 'Your Order item and placeorder is successfull register Thanking you for Purchasing  product from for site.... check your Myorder for more detail<a href="http://127.0.0.1:8000/my_order?orderno=order">myorder</a>'
    recipient_list = [email_id]  # Replace with the recipient's email address
    nobj=Newcartadd.objects.filter(userid=userobj,status=0).update(status=1)
    send_custom_email(subject, message, recipient_list)

    
    return render(req,'paymentresponsed.html')

def userId(idn):
    userid=User_regtbl.objects.get(id=idn)
    return  userid

def remove_from_cart(request):
    cid=request.GET.get('idn')
    obj=add_to_cart_table.objects.filter(id=cid)
    obj.delete()
    return redirect("/cart_view")
def booking(request):
    pid=request.GET.get('idn')
    uid=request.session['uid']
    status=request.GET.get('status')
    if status!="out of stock" :
       obj=product_upload_tbl.objects.filter(id=pid)
       obj1=User_regtbl.objects.filter(id=uid)
       return render(request,"User_booking.html",{"pro":obj,"use":obj1})
    else:
        messages.success(request, 'product is out of stock')
        return redirect("/sports_items")

def Save_booking(request):
    uid=request.session['uid']
    if request.method=="POST":
        Altnumber=request.POST.get('altphone')
        Qty=request.POST.get('quantity')
        Amount=request.POST.get('amount')
        pid=request.POST.get('proid')
        Saddress=request.POST.get('shipaddress')
        mypro=product_upload_tbl.objects.get(id=pid)
        use=User_regtbl.objects.get(id=uid)
        obj=Booking.objects.create(Alt_phone=Altnumber,quantity=Qty,Amount=Amount,shipping_Address=Saddress,status="notsuccess",user=use,product=mypro)
        obj.save()
    
        if obj:
       
            return render(request,"payment.html",{"book":obj})
        else:
            redirect("/booking")
    else:
        redirect("/booking")
def payment(request):
    bid=request.GET.get('idn')
    obj=Booking.objects.get(id=bid)
    obj.status="booking success"
    obj.save()
    messages.success(request, 'Booking Successfull')
    uid=request.session['uid'] 
    userid=User_regtbl.objects.get(id=uid)
    ordertrac=OrderTrac.objects.create(status="PLACED",userid=userid,orderid=obj)
    if ordertrac:
        ordertrac.save()


    return redirect("/sports_items")


def orderDetail(request):
    order_tables = OrderTable.objects.order_by('-id').all()
    usid=userId(request.session['uid'])
    placeorder=Placeoreder.objects.select_related('userid').order_by('-id').filter(userid=usid)
   
    return render(request, 'myorder/bookingdetail.html', {"order_tables":placeorder})

def orderView(request):
    if request.method=="GET":
        orderno=request.GET.get('ord')
        order_items = OrderItem.objects.order_by('-id').filter(order_number=orderno)
        return render(request,'myorder/orderdetail.html',{'order':order_items})
    else:
        return redirect("/bookingdetails")
#order tracking
# def orderDetail(request):
#     uid=request.session['uid']
#     bkid=request.GET.get('bkid')
#     bk=Booking.objects.get(id=bkid)
#     order=OrderTrac.objects.select_related('orderid').filter(userid=uid,orderid=bk)

    
#     if request.method == 'POST':
#         # new_status = request.POST.get('status')
#         # order.status = new_status
#         # order.save()
#         return render(request, 'order/order_detail.html', {'order': order})
    
#     return render(request, 'orderTrac/orderdetail.html', {'order': order})
#------------------------------------------------xxxxxxxxxxxxxxxxxxxxxxxxxx-------------------------------------
def my_order(request):
    uid=request.session['uid']
    use=User_regtbl.objects.get(id=uid)
    obj=Booking.objects.all()
    if obj:
        return render(request,"User_myorder.html",{"view":obj})
    else:
        return redirect("/sports_items")
def cancel_booking_sports_item(request):
    bid=request.GET.get('idn')
    obj=Booking.objects.get(id=bid)
    if(obj.arrival_date <= timezone.make_aware(datetime.now()) and obj.status=="delivered"):
             messages.success(request, 'Not Possible To Cancel')
             return redirect("/my_order")
    else:
        obj.delete()
        messages.success(request, 'booking cancelled and your refund will be received as soon as possible the product will collect from you with in 10 days')
        return redirect("/my_order")
def complaint_reg_view(request):
    print("complaint")
    bid=request.GET.get('ordid')

    obj=OrderItem.objects.filter(id=bid)
    objs=OrderItem.objects.get(id=bid)
    plac=Placeoreder.objects.get(trackno=objs.order_number)
    if obj:
        if plac.status=="Completed":
            return render(request,"Complaint_reg.html",{"view":obj})
        else:
            return HttpResponse("Order status should be completed <a href='/my_order'>Back<a/>")
    else:
        return redirect("/my_order")
    


def save_complaint(request):
    if request.method=="POST":
        complain=request.POST.get('complaint')
        ccimage=request.FILES.get('cimage')
        bid=request.POST.get('idn')
        obj=OrderItem.objects.get(id=bid)
        obj1=Itemseller_reg_tbl.objects.get(id=obj.product_name.sellerid)
        mycom=complaint_reg_tbl.objects.create(complaint=complain,cimage=ccimage,book=obj,seller=obj1,status="notsolved")
        mycom.save()
        if mycom:
             messages.success(request, 'complaint registered please wait for our reply')
             return redirect("/my_order")
        else:
            return render("/cart_view")
    else:
        return redirect("/my_order")
def complaint_view(request):
    uid=request.session['uid']
    obj=User_regtbl.objects.get(id=uid)
    mycom=complaint_reg_tbl.objects.filter(book__user=obj)
    if mycom:
        return render(request,"User_complaint.html",{"view":mycom})
    else:
        return redirect("/my_order")
def user_home_view(request):
    return render(request,"User_home.html")
def Event_view(request):
    today=datetime.today()
    obj=Event_reg_tbl.objects.filter(edate__gte=today,em__Approve=True)
    if obj:
       return render(request,"User_Event_view.html",{"view":obj})
    else:
        return redirect("/user_home_view")
def event_book(request):
    uid=request.session['uid']
    if request.method=="POST":
        eid=request.POST.get('eid')
        noticket=request.POST.get('ticketno')
        ticketam=request.POST.get('tm')
        amount= int(noticket)*int(ticketam)
        event=Event_reg_tbl.objects.get(id=eid)
        userob=User_regtbl.objects.get(id=uid)
        if (int(noticket)<=event.avl_tickets):
          obj=book_event_tbl.objects.create(event=event,audient=userob,ticketno=noticket,amount=amount)
          obj.save()
          if obj:
            return render(request,"Event_payment.html",{"book":obj})
        else:
            messages.success(request,'no tickets available')
            return redirect("/Event_view")
    else:
        return redirect("/Event_view")
def Event_pay_submit(request):
    if request.method=="POST":
        bid=request.POST.get('idn')
        ticketno=request.POST.get('tn')
        obj=book_event_tbl.objects.get(id=bid)
        even=Event_reg_tbl.objects.get(id=obj.event.id)
        if obj:
            if (int(ticketno)<=even.avl_tickets):
              obj.status="payed"
              obj.save()
              even.avl_tickets=even.avl_tickets-int(ticketno)
              even.save()
              uid=request.session['uid']
              usr=User_regtbl.objects.get(id=uid)
              email=usr.eml
              amount=request.POST.get('amount')
              message="Booking successfully, No of Tickets:"+str(ticketno)+"Price:"+str(amount)+"Location:"+str(even.eloc)+"Event idno"+str(even.id)
              send_custom_email("Event Booking",message,[email])
              messages.success(request,'Booking success')
              return redirect("/Event_view")
            else:
                messages.success(request,'no tickets available')
                return redirect("/Event_view")

        else:
            messages.success(request,'Something went wrong')
            return redirect("/Event_view")
def event_mybooking_view(request):
    uid=request.session['uid']
    obj=book_event_tbl.objects.filter(audient__id=uid,status="payed",cancel='Nill')
    if obj:
        return render(request,"User_event_my_booking.html",{"view":obj})
    else:
        messages.success(request,'no bookings')
        return redirect("/Event_view")
def cdatetime(evt):
    current_datetime = datetime.now()
    return current_datetime <= evt.replace(tzinfo=None)
def event_cancel(req):
    eid=req.POST.get("eid")
    obj=book_event_tbl.objects.get(id=eid)
    evtdate=obj.event.edate
    input_time=evtdate
    
    print("eventbk",evtdate)
    ct=cdatetime(evtdate)
    #input_datetime = datetime.strptime(input_time, "%b. %d, %Y, %I:%M %p")
    if obj and ct :
        obj.cancel="cancel"
        obj.save()
        messages.success(req,"Event is Canceled,amount will refund with in one week") 
        return redirect("/event_mybooking_view")   
    else:
        messages.success(req,"Event Can't  Canceled") 
def event_search(request):
    today=datetime.today()
    if request.method=="POST":
        dist=request.POST.get('dist')
        obj=Event_reg_tbl.objects.filter(dist=dist,edate__gte=today)
        if obj:
            return render(request,"User_Event_view.html",{"view":obj})
        else:
             messages.success(request,'Event Not Found')
             return redirect("/Event_view")
def User_academy_view(request):
    obj=Academy_reg_tbl.objects.filter(Approve=True)
    if obj:
        return render(request,"User_Academy_view.html",{"view":obj})
    else:
        return render(request,"User_home.html")
def Admission_form_view(request):
    aid=request.GET.get('idn')
    status=request.GET.get('status')
    if status=="seat available":
      return render(request,"User_addmission_form.html",{"view":aid})
    else:
        messages.success(request,'seat not available')
        return redirect("/User_academy_view")
def User_academy_admission(request):
    uid=request.session['uid']
    if request.method=="POST":
        btn= request.POST.get('submit')
        print("btn",btn)
        if btn=="Submit":
            fname=request.POST.get('fname')
            lname=request.POST.get('Lname')
            mobile=request.POST.get('mob')
            eml=request.POST.get('email')
            Age=request.POST.get('Age')
            Gen=request.POST.get('Gender')
            Address=request.POST.get('Address')
            aid=request.POST.get('aid')
            user=User_regtbl.objects.get(id=uid)
            academy=Academy_reg_tbl.objects.get(id=aid)
            obj=Academy_admission_tbl.objects.create(fname=fname,lname=lname,mob=mobile,ag=Age,ad=Address,gn=Gen,eml=eml,academy=academy,user=user)
            if obj:
                messages.success(request,'Addmission Successfull Staff From Academy Contact Soon')
                return redirect("/User_academy_view")
            else:  
                messages.success(request,'Addmission Not Successfull Please try again')
                return redirect("/User_academy_view")
        elif btn=='Reset':
            aid=request.POST.get('aid')
            return render(request,"User_addmission_form.html",{"view":aid})  

    else:
        aid=request.POST.get('aid')
        return render(request,"User_addmission_form.html",{"view":aid})  
def academy_search(request):
    if request.method=="POST":
        dist=request.POST.get('dist')
        obj=Academy_reg_tbl.objects.filter(dist=dist)
        if obj:
            return render(request,"User_Academy_view.html",{"view":obj})
        else:
            messages.success(request,"Academy not Found")
            return redirect("/User_academy_view")
    else:
        return redirect("/User_academy_view")
def My_addmision_view(request):
    uid=request.session['uid']
    obj=Academy_admission_tbl.objects.filter(user__id=uid)
    if obj:
        return render(request,"User_my_Addmission.html",{"view":obj})
    else:
        messages.success(request,'Addmission Not Successfull Please try again')
        return redirect("/User_academy_view")
def post_view(request):
    obj=posts_tbl.objects.filter(approve=True)
    comment=comments_tbl.objects.filter()
    if obj:
        return render(request,"post_view.html",{"view":obj,"cmnt":comment})
    else:
        messages.success(request,'no posts')
        return render(request,"User_home.html")

def make_post(request):
    uid=request.session['uid']
    if request.method=="POST":
        pimgs=request.FILES.get('pimg')
        content=request.POST.get('content')
        user=User_regtbl.objects.get(id=uid)
        obj=posts_tbl.objects.create(pimg=pimgs,Pcaption=content,user=user)
        obj.save()
        if obj:
            return redirect("/post_view")
        else:
            return render(request,"make_post.html")
    else:
        return render(request,"make_post.html")
def comment(request):
    uid=request.session['uid']
    if request.method=="POST":
        pid=request.POST.get('pid')
        comment=request.POST.get('comment')
        post=posts_tbl.objects.get(id=pid)
        user=User_regtbl.objects.get(id=uid)
        obj=comments_tbl.objects.create(user=user,comment=comment,post=post)
        if obj:
            return redirect("/post_view")
        else:
            return redirect("/post_view")
    else:
        return render(request,"User_home.html")
from Turf . models import turf_reg_tbl,slot_tbl
def user_turf_view(request):
    turf=turf_reg_tbl.objects.filter(Approve=True)
    if turf:
        slot=slot_tbl.objects.filter(status="no issue")
        return render(request,"user_turf_view.html",{"view":turf,"slot":slot})
    else:
        messages.success(request,'no turfs')
        return render(request,"User_home.html")
from django.utils import timezone
def turf_book(request):
    uid=request.session['uid']
    if request.method=="POST":
        tid=request.POST.get('tid')
        bdate=request.POST.get('bdate')
        slot=request.POST.get('slot')
        user=User_regtbl.objects.get(id=uid)
        turf=turf_reg_tbl.objects.get(id=tid)
        slotob=slot_tbl.objects.get(id=slot)
        today = datetime.now().date()
        six_days_later = today + timedelta(days=6)
        date = datetime.strptime(bdate, '%Y-%m-%d').date() 
        if date <= six_days_later or (date== date.today() and slotob.stime<timezone.now().time()):
           if  turf_booking_tbl.objects.filter(turf__id=tid,bdate=bdate,stime__lt=slotob.etime,etime__gt=slotob.stime,status="paid").exists():
               messages.success(request,'already booked choose another slot')
               return redirect("/user_turf_view")
           else:
            if turf and slotob:
              obj=turf_booking_tbl.objects.create(sid=slotob.id,bdate=bdate,user=user,turf=turf,stime=slotob.stime,etime=slotob.etime,amount=slotob.amount)
              obj.save()
              return render(request,"turf_payment.html",{"book":obj})
            else:
                return redirect("/user_turf_view")

        else:
          messages.success(request,'only allowed to book dates within 6 days')
          return redirect("/user_turf_view")
    else:
        return redirect("/user_turf_view")
def turf_pay(request):
    uid=request.session['uid']
    if request.method=="POST":
        idn=request.POST.get('idn')
        edate=request.POST.get('expiry-date')
        user=User_regtbl.objects.get(id=uid)
        obj=turf_booking_tbl.objects.get(id=idn)
        date = datetime.strptime(edate, '%Y-%m-%d').date() 
        if obj and date>date.today():
            obj.status="paid"
            obj.save()
            subject = 'Turf Booking Confirmation'
            message = f'Dear {user.eml},\n\nYour booking for {obj.turf.tname} has been confirmed.your slot is {obj.stime}-{obj.etime} and book date {obj.bdate} Thank you for choosing our service!\n\nRegards,\nThe Turf Booking Team'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.eml]
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            messages.success(request,'booking success')
            return redirect("/user_turf_view")
        else:
            messages.success(request,'card is expired')
            return redirect("/user_turf_view")
    else:
        return redirect("/user_turf_view")
def turf_my_booking(request):
    uid=request.session['uid']
    obj=turf_booking_tbl.objects.filter(user__id=uid,status="paid")
    if obj:
        return render(request,"user_turf_booking_view.html",{"view":obj})
    else:
        return redirect("/user_turf_view")
def turf_cancel_book(request):
    uid=request.session['uid']
    if request.method=="POST":
        bid=request.POST.get('bid')
        obj=turf_booking_tbl.objects.get(user__id=uid,id=bid)
        if obj.bdate>date.today():
          obj.delete()
          messages.success(request,'booking cancelled your refund is progressing')
          return redirect("/turf_my_booking")
        else:
            messages.success(request,'not possible to  cancell')
            return redirect("/turf_my_booking")

    else:
        return redirect("/turf_my_booking")
def p_search(request):
    if request.method=="POST":
        search=request.POST.get('pnm')
        catid=Pcategory.objects.get(cname=search)
        cat=Pcategory.objects.all()
        products=product_upload_tbl.objects.select_related('catid').filter(catid=catid).exclude(status="delete")
        if products:
            return render(request,"newuser_item_view.html",{"view":products,"cat":cat}) 
        else:
            messages.success(request,'no product')
            return redirect("/sports_items")
    else:
        return redirect("/sports_items")
def turf_search(request):
    if request.method=="POST":
        dist=request.POST.get('dist')
        turf=turf_reg_tbl.objects.filter(Approve=True,dist=dist)
        if turf:
           slot=slot_tbl.objects.filter(status="no issue")
           return render(request,"user_turf_search.html",{"view":turf,"slot":slot})
        else:
          messages.success(request,"Turff Not Found")
          return redirect("/user_turf_view")
    else:
         return redirect("/user_turf_view")
def my_post_view(request):
    uid=request.session['uid']
    obj=posts_tbl.objects.filter(user__id=uid,approve=True)
    comment=comments_tbl.objects.all()
    if obj:
        return render(request,"my_post.html",{"view":obj,"cmnt":comment})
    else:
        messages.success(request,'no my posts')
        return redirect("/post_view")

def delete_post(request):
    pid=request.GET.get('idn')
    obj=posts_tbl.objects.get(id=pid)
    if obj:
        obj.delete()
        return redirect("/my_post_view")
    else:
        return redirect("/my_post_view")
def user_profile(request):
    uid=request.session['uid']
    obj=User_regtbl.objects.filter(id=uid)
    if obj:
        return render(request,"User_profile.html",{'view':obj})
    else:
        return render(request,"User_home.html")
    
def nwcrtdelete(request):
    
    cid=request.GET.get('nwid')
    obj=Newcartadd.objects.filter(id=cid)
    obj.delete()
    return redirect("/cart_view")
def user_logout(req):
    req.session['uid']=" "
    return redirect("/")
         
def orderCancel(req):
    # trno=req.GET.get('ordno')
    # cobj=Placeoreder.objects.get(trackno=trno)
    # cobj.status="Cancel"
    # cobj.save()
    

    # pobj=Placeoreder.objects.filter(trackno=trno,status="Cancel")
    return render(req,'item_cancel_response.html')
def discard(req):
    trno=req.GET.get('ordno')
    cobj=Placeoreder.objects.get(trackno=trno)
    if cobj.status=="Completed":
        msg="Order is been Cancel ,Product will soon  recollected and refund"
    elif cobj.status=="Cancel":
        msg="Already Canceled"
    else:
        msg="Refunded Soon"    

    cobj.status="Cancel"
    cobj.save()
    

    pobj=Placeoreder.objects.filter(trackno=trno,status="Cancel")
    return render(req,'order_cancel/item_cancel_response.html',{'data':pobj,"msg":msg})

        
#contact-------------------------------------------------------------------------------------------------------
from . models import Contact    
def contact(request):
    if request.method == 'POST':
 
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
            message=message.replace("\n"," ")
            nmessage=message.replace("\r"," ")

            send_custom_email(message,subject,[email])

            # Save the data 
            contact = Contact(name=name, email=email, subject=subject, message=str(nmessage))
            contact.save()

            # Redirect after successful form submission
            return redirect('/contact_success')
        except Exception  as e:
             return HttpResponse(e)

 

    return render(request, 'contact/contact.html', {'form':''})


def contact_success(req):
    return render(req,'contact/contact_success.html')



    


    


    
          




        

    


            




        

          

          
        





        

        





        
    
    


      




    






        
        
  
     
        
        
            
    


    





    
    










    
    






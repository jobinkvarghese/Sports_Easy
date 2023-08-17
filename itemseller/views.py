from django.shortcuts import render,redirect
from itemseller . models import Itemseller_reg_tbl
from itemseller . models import product_upload_tbl,Pcategory
from User . models import complaint_reg_tbl,Booking,Placeoreder,OrderTable,OrderItem
from django . contrib import messages
# Create your views here.
def home_view(request):
    return render(request,"index.html")
def itemseller_reg(request):
    if request.method=='POST':
        sname=request.POST.get('seller_name')
        mobile=request.POST.get('phone')
        eml=request.POST.get('email')
        Address=request.POST.get('Address')
        pas=request.POST.get('ps1')
        cpass=request.POST.get('ps2')
        if Itemseller_reg_tbl.objects.filter(Email=eml).exists():
            messages.success(request, 'Another Account Has Similar Email Id')
            return render(request,"itemseller_reg.html")
        else:
         obj=Itemseller_reg_tbl.objects.create(sellername=sname,mobile=mobile,Address=Address,Email=eml,password=pas,confirm_password=cpass)
         obj.save()
         if obj:
            return render(request,"itemseller_login.html")
         else:
            return render(request,"itemseller_reg.html")
    else:
        cat=Pcategory.objects.all()
        return render(request,"itemseller_reg.html")
    
def createCategory(req):
    if req.method=="POST":
        ct=req.POST.get('cat')
        ctd=Pcategory.objects.create(cname=ct)
        if ctd:
           ctd.save()
           return render(req,'regcategory.html',{'msg':"category created"}) 
        else:
            return render(req,'regcategory.html',{'msg':"category Not created"}) 

    return render(req,'regcategory.html',{'msg':""})    
def itemseller_login(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        obj=Itemseller_reg_tbl.objects.filter(Email=eml,password=psw,Approve=True)
        if obj:
            for l in obj:
                sid=l.id
                request.session['sid']=sid
            return render(request,"itemseller_home.html")
        else:
            messages.success(request,'Login Failed')
            return render(request,"itemseller_login.html")
    else:
        return render(request,"itemseller_login.html")

def product_upload(request):
    sid=request.session['sid']
    if request.method=='POST':
        sname=request.POST.get('name')
        productname=request.POST.get('pname')
        pamount=request.POST.get('amount')
        details=request.POST.get('details')
        pimage=request.FILES.get('image')
        cat=Pcategory.objects.get(id=request.POST.get('cat'))
        seller=Itemseller_reg_tbl.objects.get(id=sid)
        obj=product_upload_tbl.objects.create(catid=cat,sellerid=sid,sellername=sname,seller=seller,productname=productname,productamount=pamount,productdetails=details,productimage=pimage)
        obj.save()
        if obj:
            return redirect("/product_view")
        else:
            cat=Pcategory.objects.all()
            return render(request,"product_upload.html",{'cat':cat})
    else:
        cat=Pcategory.objects.all()
        return render(request,"product_upload.html",{'cat':cat})
def product_view(request):
    id=request.session['sid']
    print("sellerid",id)
    slid=Itemseller_reg_tbl.objects.get(id=id)
    mypro=product_upload_tbl.objects.filter(sellerid=slid.id).exclude(status="delete")
    return render(request,"itemseller_myproduct.html",{"view":mypro})   
def delete(request):
    idno=request.GET.get('idn')
    obj=product_upload_tbl.objects.get(id=idno)
    obj.status="delete"
    obj.save()
    return redirect("/product_view")
def edit(request):
    idno=request.GET.get('idn')
    obj=product_upload_tbl.objects.filter(id=idno)
    return render(request,"product_upload2.html",{"data":obj})
def product_update(request):
    if request.method=="POST":
        idn=request.POST.get('idno')
        sname=request.POST.get('name')
        productname=request.POST.get('pname')
        pamount=request.POST.get('amount')
        details=request.POST.get('details')
        pimage=request.FILES.get('image')
        status=request.POST.get('status')
        obj=product_upload_tbl.objects.get(id=idn)
        obj.sellername=sname
        obj.productname=productname
        obj.productamount=pamount
        obj.productdetails=details
        obj.status=status
        if pimage!=None:
         obj.productimage=pimage
        obj.save()
        return redirect("/product_view")
    return render(request,"product_upload2.html")
def User_complaint_view(request):
    sid=request.session['sid']
    obj=complaint_reg_tbl.objects.filter(seller__id=sid).exclude(status="rejected").exclude(status="solved")
    if obj:
        return render(request,"itemseller_user_complaint.html",{"view":obj})
    else:
        messages.success(request, 'complaint box is empty nothing to solve')
        return render(request,"itemseller_home.html")
def Update_complaint(request):
    if request.method=="POST":
         btnvalue=request.POST.get('btn')
         updates=request.POST.get('updates')
         cid=request.POST.get('cid')
         obj=complaint_reg_tbl.objects.get(id=cid)
         if btnvalue=="rejected":
               if obj:
                   obj.status="rejected"
                   obj.save()
                   return redirect("/user_complaint_view") 
               else:
                 return redirect("/user_complaint_view")
         if btnvalue=="solved":
               if obj:
                   obj.status="solved"
                   obj.save()
                   return redirect("/user_complaint_view") 
               else:
                 return redirect("/user_complaint_view")
         if btnvalue=="updt":
               if obj:
                   obj.status=updates
                   obj.save()
                   print(updates,"updates comlaint")
                   return redirect("/user_complaint_view") 
               else:
                 return redirect("/user_complaint_view")
def solved_complaint_view(request):
    sid=request.session['sid']
    obj=complaint_reg_tbl.objects.filter(seller__id=sid,status="solved")
    if obj:
        return render(request,"itemseller_solved_complaints.html",{"view":obj})
    else:
        return redirect("/user_complaint_view")      
def itemseller_booking_view(request):
    sid=request.session['sid']
    seller=Itemseller_reg_tbl.objects.get(id=sid)
    obj = OrderItem.objects.select_related("sellerid").order_by('-id').filter(sellerid=seller).exclude(status='Completed')
    

   
    if obj:
        return render(request,"itemseller_view_booking.html",{"view":obj})    
    else:
        return render(request,"itemseller_home.html")
    
def orderView(request):
    if request.method=="GET":
        orderno=request.GET.get('ord')
        sid=request.session['sid']
        seller=Itemseller_reg_tbl.objects.get(id=sid)
        order_items = OrderItem.objects.select_related("sellerid").order_by('-id').filter(order_number=orderno,sellerid=seller)
        return render(request,'seller/orderdetail.html',{'order':order_items})
    else:
        return redirect("/itemseller_booking_view")    
def item_booking_delivery(request):   
    if request.method=="POST":
        bid=request.POST.get('bid')
        btnvalue=request.POST.get('btn')
        obj=Booking.objects.get(id=bid)
        if obj:
          if btnvalue=="cancel":
            obj.status="order canceled by seller your payment is refunded"  
            obj.save() 
            return redirect("/itemseller_booking_view")
         
          if btnvalue=="delivered":
            obj.status="delivered"  
            obj.save()
            return redirect("/itemseller_booking_view")   
        else:
            return redirect("/itemseller_booking_view")
    else:
         return redirect("/itemseller_booking_view")

    
def delivered_products(request):
    sid=request.session['sid']
    obj=OrderItem.objects.filter(sellerid=sid,status="Completed")
    if obj:
        return render(request,"delivered_products.html",{"view":obj})
    else:
        messages.success(request, 'delivered products box is empty')
        return render(request,"itemseller_home.html")
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect("/")    
def itemseller_home_view(request):
    return render(request,"itemseller_home.html")    
def prodelete(req):
    return 
    
            
        
  
    
    
       





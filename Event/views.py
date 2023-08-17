from django.shortcuts import render,redirect
from .models import Event_reg_tbl,Event_manager_tbl
from django . contrib import messages
from User.models import book_event_tbl
from  datetime import datetime

# Create your views here.
def Event_manager_reg_view(request):
    return render(request,"Event_manager_reg.html")
def Event_manage_reg(request):
    if request.method=="POST":
        emn=request.POST.get('ename')
        eaddress=request.POST.get('eaddress')
        emob=request.POST.get('mobile')
        email=request.POST.get('email')
        psw=request.POST.get('eps1')
        cpsw=request.POST.get('eps2')
        if Event_manager_tbl.objects.filter(email=email).exists():
            messages.success(request, 'Another Account Has Similar Email Id')
            return redirect("/Event_manager_reg_view")
        obj=Event_manager_tbl.objects.create(emname=emn,email=email,Address=eaddress,mobile=emob,pass1=psw,pass2=cpsw) 
        obj.save()
        if obj:
            messages.success(request,'Event registered Successfull')
            return redirect("/Event_login_view")
        else:
            return redirect("/Event_manager_reg_view")
    else:
        return redirect("/Event_manager_reg_view")
def Event_manage_login(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        obj=Event_manager_tbl.objects.filter(email=eml,pass1=psw,Approve=True)
        if obj:
            for l in obj:
                eid=l.id
                request.session['eid']=eid
            return render(request,"Event_home.html")
        else:
            messages.success(request,'Login Failed')
            return render(request,"Event_manage_login.html")
    else:
        return render(request,"Event_manage_login.html")

def Event_reg_view(request):
    return render(request,"Event_reg.html")
def Event_reg(request):
    eid=request.session['eid']
    if request.method=="POST":
        enm=request.POST.get('ename')
        eim=request.FILES.get('eimg')
        dist=request.POST.get('dist')
        eaddress=request.POST.get('eaddress')
        eedate=request.POST.get('edate')
        emob=request.POST.get('mobile')
        eloc=request.POST.get('loc')
        edetail=request.POST.get('dtl')
        email=request.POST.get('email')
        amount=request.POST.get('amount')
        ticket=request.POST.get('ticket')
        em=Event_manager_tbl.objects.get(id=eid)
        obj=Event_reg_tbl.objects.create(ename=enm,em=em,eemail=email,eimage=eim,edate=eedate,eaddress=eaddress,mobile=emob,eloc=eloc,details=edetail,ticket=ticket,dist=dist,emid=eid,avl_tickets=ticket,ticket_amount=amount) 
        obj.save()
        if obj:
            messages.success(request,'Event Added Successfull')
            return redirect("/Event_reg_view")
        else:
             return render(request,"Event_home.html")
    else:
        return render(request,"Event_home.html")
    
def Event_login_view(request):
    return render(request,"Event_manage_login.html")
def my_event_view(request):
    emid=request.session['eid']
    obj=Event_reg_tbl.objects.filter(emid=emid).exclude(Approve=False)
    if obj:
        return render(request,"my_event_view.html",{"view":obj})
    else:
        messages.success(request,'no events')
        return render(request,"Event_home.html")
def  event_booking_view(request):
    emid=request.session['eid']
    obj=Event_reg_tbl.objects.filter(emid=emid).exclude(Approve=False)
    if obj:
      return render(request,"Event_booking_eventname_view.html",{"view":obj})
    else:
        messages.success(request,'no bookings')
        return redirect("/event_home") 
def event_home(request):
    return render(request,"Event_home.html")
def eventDelete(req):
    idn=req.GET.get("idno")
    obj=Event_reg_tbl.objects.get(id=idn)
    obj.Approve=False
    obj.save()
    return redirect("/my_event_view")
def event_booking_table(request):
    emid=request.session['eid']
    if request.method=="POST":
        evid=request.POST.get('evid')
        obj=book_event_tbl.objects.filter(event__id=evid,event__emid=emid,status="payed")
        if obj:
            return render(request,"Event_view_booking.html",{"view":obj})
        else:
            messages.success(request,'no bookings')
            return redirect("/event_booking_view")
    else:
        return render(request,"Event_home.html") 
def update_event(request):
    emid=request.session['eid']
    if request.method=="POST":
        sts=request.POST.get('sts')
        idn=request.POST.get('idn')
        btn=request.POST.get('btn')
        obj=Event_reg_tbl.objects.get(emid=emid,id=idn)
        if obj:
            if btn=="Update":
                obj.status=sts
                obj.save()
                return redirect("/my_event_view")
            elif btn=="delete":
                if obj.edate<=datetime.today():
                    obj.delete()
                    return redirect("/my_event_view")
                else:
                     return redirect("/my_event_view")
            else:
                return redirect("/my_event_view")
        else:
            return redirect("/my_event_view")
    else:
        return redirect("/my_event_view")
    
            



    











    









        

               

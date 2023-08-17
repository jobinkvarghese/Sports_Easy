from django.shortcuts import render,redirect
from . models import turf_reg_tbl,slot_tbl
from django . contrib import messages
from User . models import turf_booking_tbl

# Create your views here.
def Turf_reg(request):
    if request.method=="POST":
        tname=request.POST.get('tname')
        temail=request.POST.get('temail')
        tloc=request.POST.get('tloc')
        timg=request.FILES.get('timg')
        tmob=request.POST.get('mobile')
        tdetails=request.POST.get('tdetails')
        taddress=request.POST.get('taddress')
        dist=request.POST.get('dist')
        ps1=request.POST.get('ps1')
        ps2=request.POST.get('ps2')
        if turf_reg_tbl.objects.filter(temail=temail).exists():
            messages.success(request, 'Another Account Has Similar Email Id')
            return render(request,"Turf_reg.html")
        else: 
          obj=turf_reg_tbl.objects.create(tname=tname,timg=timg,tloc=tloc,tdetails=tdetails,temail=temail,tmob=tmob,dist=dist,taddress=taddress,ps1=ps1,ps2=ps2)
          obj.save()
          if obj:
            return render(request,"Turf_login.html")
          else:
           return render(request,"Turf_reg.html")
    else:
        return render(request,"Turf_reg.html")
def Turf_login(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        obj=turf_reg_tbl.objects.filter(temail=eml,ps1=psw,Approve=True)
        if obj:
            for l in obj:
                tid=l.id
                request.session['tid']=tid
            return render(request,"Turf_home.html",{"view":obj})
        else:
            messages.success(request,'incorrect email or password')
            return render(request,"Turf_login.html")
    else:
        return render(request,"Turf_login.html")
def slot_add(request):
   tid=request.session['tid']
   if request.method=="POST":
      stime=request.POST.get('stime')
      etime=request.POST.get('etime')
      amount=request.POST.get('samount')
      turf=turf_reg_tbl.objects.get(id=tid)
      if slot_tbl.objects.filter(turf=turf,stime__lt=etime,etime__gt=stime).exists():
            messages.success(request,'similar slot exist')
            return render(request,"Turf_slot_add.html")
      else:
       obj=slot_tbl.objects.create(stime=stime,etime=etime,turf=turf,amount=amount)
       obj.save()
       if obj:
        messages.success(request,'slot added succefull')
        return render(request,"Turf_slot_add.html")
       else:
        messages.success(request,'slot not succefull')
        return render(request,"Turf_slot_add.html")
   else:
      return render(request,"Turf_slot_add.html")  
         
def turf_home(request):
   return render(request,"Turf_home.html")
def slot_view(request):
   tid=request.session['tid']
   obj=slot_tbl.objects.filter(turf__id=tid)
   if obj:
      return render(request,"Turf_my_slot.html",{"view":obj})
   else:
      return render(request,"Turf_home.html")
def slot_edit(request):
   if request.method=="POST":
      btn=request.POST.get('btn')
      sid=request.POST.get('sid')
      status=request.POST.get('status')
      if btn=="delete":
         obj=slot_tbl.objects.get(id=sid)
         obj.delete()
         return redirect("/slot_view")
      elif btn=="update":
        obj=slot_tbl.objects.get(id=sid)
        if status!='':
          obj.status=status
          obj.save()
          return redirect("/slot_view")
        else:
           return redirect("/slot_view")
   else:
    return redirect("/slot_view") 
def turf_view_booking(request):
   tid=request.session['tid']
   obj=turf_booking_tbl.objects.filter(turf__id=tid,status="paid")
   if obj:
      return render(request,"Turf_view_booking.html",{"view":obj})
   else:
      messages.success(request,'slot not succefull')
      return render(request,"Turf_home.html")
      


      
      

   
   
      




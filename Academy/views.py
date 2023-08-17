from django.shortcuts import render,redirect
from . models import Academy_reg_tbl
from User . models import Academy_admission_tbl
from django . contrib import messages
# Create your views here.
def Academy_reg(request):
    if request.method=="POST":
        aname=request.POST.get('aname')
        adetail=request.POST.get('dtl')
        aimg=request.FILES.get('aimg')
        dist=request.POST.get('dist')
        address=request.POST.get('aaddress')
        eml=request.POST.get('aemail')
        loc=request.POST.get('loc')
        amob=request.POST.get('mobile')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if Academy_reg_tbl.objects.filter(Aemail=eml).exists():
            messages.success(request, 'Another Account Has Similar Email Id')
            return render(request,"Academy_reg.html")
        obj=Academy_reg_tbl.objects.create(Aname=aname,Adetails=adetail,Amob=amob,Aimg=aimg,Aloc=loc,Aemail=eml,password=pass1,cpass=pass2,Address=address,dist=dist)
        obj.save()
        if obj:
            return render(request,"Academy_login.html")
        else:
            return render(request,"Academy_reg.html")
    else:
         return render(request,"Academy_reg.html")
def Academy_login(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        obj=Academy_reg_tbl.objects.filter(Aemail=eml,password=psw,Approve=True)
        if obj:
            for i in obj:
                request.session['aid']=i.id
            return render(request,"Academy_home.html")
        else:
            messages.success(request,'Login Failed')
            return render(request,"Academy_login.html")
    else:
        return render(request,"Academy_login.html")
def Academy_profile_view(request):
    aid=request.session['aid']
    obj=Academy_reg_tbl.objects.filter(id=aid)
    if obj:
        return render(request,"Academy_profile.html",{"view":obj})
    else:
        return render(request,"Academy_home.html")
def Academy_update_view(request):
    aid=request.session['aid']
    obj=Academy_reg_tbl.objects.filter(id=aid)
    if obj:
        return render(request,"Academy_profile_update.html",{"view":obj})
    else:
        return redirect("/Academy_profile_view")

def Academy_update(request):
    aid=request.session['aid']
    if request.method=="POST":
        aname=request.POST.get('aname')
        adetail=request.POST.get('dtl')
        aimg=request.FILES.get('aimg')
        dist=request.POST.get('dist')
        address=request.POST.get('aaddress')
        eml=request.POST.get('aemail')
        loc=request.POST.get('loc')
        status=request.POST.get('status')
        amob=request.POST.get('mobile')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        obj=Academy_reg_tbl.objects.get(id=aid)
        if obj:
            obj.Aname=aname
            obj.Adetails=adetail
            if aimg!=None:
             obj.Aimg=aimg
            obj.dist=dist
            obj.Address=address
            obj.Aloc=loc
            obj.status=status
            obj.Aemail=eml
            obj.Amob=amob
            obj.password=pass1
            obj.cpass=pass2
            obj.save()
            return redirect("/Academy_profile_view")

        else:
            return redirect("/Academy_update_view")
    else:
         return redirect("/Academy_update_view")

def Academy_home_view(request):
    return render(request,"Academy_home.html")
def academy_booking_view(request):
    aid=request.session['aid']
    obj=Academy_admission_tbl.objects.filter(academy__id=aid)
    if obj:
        return render(request,"Academy_my_addmission.html",{"view":obj})
    else:
        return render(request,"Academy_my_addmission.html")










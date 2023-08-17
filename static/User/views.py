from django.shortcuts import render
from . models import reg_tbl
# Create your views here.
def index(request):
    return render(request,"index.html")
def User_reg(request):
    if request.method=='POST':
        fn=request.POST.get('fname')
        ln=request.POST.get('Lname')
        Age1=request.POST.get('Age')
        Address=request.POST.get('Address')
        mobile1=request.POST.get('mob')
        email=request.POST.get('email')
        password=request.POST.get('password')
        Cpass=request.POST.get('c_password')
        obj=reg_tbl.objects.create(fname=fn,Lname=ln,Age=Age1,Address=Address,mobile=mobile1,Email=email,password=password, confirm_password=Cpass)
        obj.save()
        if obj:
            return render(request,"User_login.html")
        else:
            return render(request,"user_reg.html")
    else:
        return render(request,"user_reg.html")   
def User_login(request):
    if request.method=="POST":
        eml=request.POST.get("email")
        psw=request.POST.get("password")
        obj=reg_tbl.objects.filter(Email=eml,password=psw)
        if obj:
            return render(request,"User_home.html")
        else:
            return render(request,"User_login.html")
    else:
        return render(request,"User_login.html")


            
   

   





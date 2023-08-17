from django.shortcuts import render,redirect
from django.http import HttpResponse
from itemseller . models import Itemseller_reg_tbl
from Turf.models import turf_reg_tbl
from Event . models import Event_manager_tbl
from Academy . models import Academy_reg_tbl
from User.models import Booking,User_regtbl
from User.models import OrderTrac,OrderTable,OrderItem,Placeoreder,posts_tbl,comments_tbl,Contact
from .models import Admintbl
from .utils import send_custom_email
#send mail 
from django.core.mail import send_mail
from django . contrib import messages
# Create your views here.
def Admin(request):
    if request.method=='POST':
        eml=request.POST.get('email')
        psw=request.POST.get('password')
        if eml and psw:
            obj=Admintbl.objects.filter(email=eml,password=psw)
            if len(obj)>0:
                return render(request,"Admin_home.html")
            else:
                return HttpResponse("Access Denied check your username and password <a href='/Admin'><<Back</a>")


            
        else:
            return render(request,"Admin_login.html")
    else:
        return render(request,"Admin_login.html")
def changeAdminpassword(request):
    if request.method=='POST':
        try:
        
            oldpsw=request.POST.get('old_password')
            newpsw=request.POST.get('new_password1')
            newpsw2=request.POST.get('new_password2')
            if oldpsw and newpsw==newpsw2:
                obj=Admintbl.objects.get(password=oldpsw)
                if obj:
                    obj.password=newpsw
                    obj.save()
                    return HttpResponse("Password Changed<a href='/Admin'>>>Login</a>")
                else:
                    return HttpResponse("Access Denied check your  password <a href='/Admin'> <<Back </a>")


                
            else:
                return HttpResponse("Access Denied check your  password and confirm password <a href='/changePass'> <<Back </a>")
        except Exception as e:
            return HttpResponse(e)    
    else:
        return render(request,"admin/AdminchangeP.html")
def Admin_itemseller_view(request):
    obj=Itemseller_reg_tbl.objects.filter(Approve=False).order_by('-id')
    if obj:
        return render(request,"Admin_itemseller_view.html",{"view":obj})
    else:
        return render(request,"Admin_itemseller_view.html")
def Admin_itemseller_approve_view(request):
    obj=Itemseller_reg_tbl.objects.filter(Approve=True).order_by('-id')
    if obj:
        return render(request,"Admin_approved_itemseller.html",{"view":obj})
    else:
        return render(request,"Admin_approved_itemseller.html")
def itemseller_approve(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        btn=request.POST.get('btn')
        obj=Itemseller_reg_tbl.objects.get(id=sid)
        if obj:
            if btn=="approve":
              obj.Approve=True
              obj.save()
              return redirect("/Admin_itemseller_view")
            elif btn=="disapprove":
              obj.Approve=False
              obj.save()
              return redirect("/Admin_itemseller_approve_view")
        else:
            return redirect("/Admin_itemseller_view")
    else:
        return redirect("/Admin_itemseller_view")
def Admin_home(request):
    return render(request,"Admin_home.html")
def Admin_turf_view(request):
    obj=turf_reg_tbl.objects.filter(Approve=False).order_by('-id')
    if obj:
        return render(request,"Admin_turf_view.html",{"view":obj})
    else:
        return render(request,"Admin_turf_view.html")
def Admin_approved_turf_view(request):
    obj=turf_reg_tbl.objects.filter(Approve=True).order_by('-id')
    if obj:
        return render(request,"Admin_approved_turf.html",{"view":obj})
    else:
        return render(request,"Admin_approved_turf.html")
def Turf_approve(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        btn=request.POST.get('btn')
        obj=turf_reg_tbl.objects.get(id=sid)
        if obj:
            if btn=="approve":
              obj.Approve=True
              obj.save()
              return redirect("/Admin_turf_view")
            elif btn=="disapprove":
              obj.Approve=False
              obj.save()
              return redirect("/Admin_approved_turf_view")
        else:
            return redirect("/Admin_turf_view")
    else:
        return redirect("/Admin_turf_view")
def Admin_event_view(request):
    obj=Event_manager_tbl.objects.filter(Approve=False).order_by('-id')
    if obj:
        return render(request,"Admin_event_view.html",{"view":obj})
    else:
        return render(request,"Admin_event_view.html")
def Admin_approved_event_view(request):
    obj=Event_manager_tbl.objects.filter(Approve=True).order_by('-id')
    if obj:
        return render(request,"Admin_approved_event.html",{"view":obj})
    else:
        return render(request,"Admin_approved_event.html")
def Event_approve(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        btn=request.POST.get('btn')
        obj=Event_manager_tbl.objects.get(id=sid)
        if obj:
            if btn=="approve":
              obj.Approve=True
              obj.save()
              return redirect("/Admin_event_view")
            elif btn=="disapprove":
              obj.Approve=False
              obj.save()
              return redirect("/Admin_approved_event_view")
        else:
            return redirect("/Admin_event_view")
    else:
        return redirect("/Admin_event_view")
def Admin_academy_view(request):
    obj=Academy_reg_tbl.objects.filter(Approve=False).order_by('-id')
    if obj:
        return render(request,"Admin_academy_view.html",{"view":obj})
    else:
        return render(request,"Admin_academy_view.html")
def Admin_approved_academy_view(request):
    obj=Academy_reg_tbl.objects.filter(Approve=True).order_by('-id')
    if obj:
        return render(request,"Admin_approved_academy.html",{"view":obj})
    else:
        return render(request,"Admin_approved_academy.html")
def Academy_approve(request):
    if request.method=="POST":
        sid=request.POST.get('sid')
        btn=request.POST.get('btn')
        obj=Academy_reg_tbl.objects.get(id=sid)
        if obj:
            if btn=="approve":
              obj.Approve=True
              obj.save()
              return redirect("/Admin_academy_view")
            elif btn=="disapprove":
              obj.Approve=False
              obj.save()
              return redirect("/Admin_approved_academy_view")
        else:
            return redirect("/Admin_academy_view")
    else:
        return redirect("/Admin_academy_view")



def orderDetail(request):


    order_tables = OrderTable.objects.order_by('-id').all()
    
    placeorder=Placeoreder.objects.select_related('userid').order_by('-id').all()

    # if request.GET['bid'] :
    #     bid=request.GET['bid']
    #     order=OrderTrac.objects.select_related('orderid').filter(orderid=bid)

    
    # if request.method == 'POST':
    #     # new_status = request.POST.get('status')
    #     # order.status = new_status
    #     # order.save()
    #     return render(request, 'order/order_detail.html', {'order': order})
    
    return render(request, 'orderTrac/bookingdetail.html', {"order_tables":placeorder})

def orderView(request):
    if request.method=="GET":
        orderno=request.GET.get('ord')
        order_items = OrderItem.objects.order_by('-id').filter(order_number=orderno)
        return render(request,'orderTrac/orderdetail.html',{'order':order_items})
    else:
        return redirect("/bookingdetails")
         
def order_update(request):
    if request.method=="POST":
        ordno=request.POST.get('ord')
        ordid=request.POST.get('ordid')
        stat=request.POST.get('sts')
        print("booking id",ordno)
        request.session['ordno']=ordno
    # order=OrderTrac.objects.get(orderid=bid)
    #     order=OrderTrac.objects.select_related('orderid').filter(orderid=bid)
        if stat=="Cancel":
            messages.success(request,"product is canceled..")
            return redirect("/bookingdetails")
        else:
            order=Placeoreder.objects.get(trackno=ordno)
            order.status=stat
            order.save()
            oritm=OrderItem.objects.get(id=ordid)
            oritm.status=stat
            oritm.save()
            plobj=Placeoreder.objects.get(trackno=ordno)
        
            email=plobj.userid.eml 
            print(email) 
       
       
        send_custom_email("order update","shipping detail",[email])
        

        return redirect("/bookingdetails")
    

    return render(request,'orderTrac/ordertracking.html')
def update_order_status(request):
    if request.method == 'POST':
        bid = request.session['bkid']
        print("booking id: ", bid)
        bk=Booking.objects.get(id=bid)
        
        order = OrderTrac.objects.filter(orderid=bk)
        for ls in order:
            orid=ls.id
            usrid=ls.userid
            status=ls.status
            print(ls.id)
        
        order=OrderTrac.objects.get(id=orid)
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        #sending email
        useremail=OrderTrac.objects.select_related('userid').get(id=orid)
        usereml=useremail.userid.eml
      
        subject = 'Order Message'
        message = "The Product Order Status:  login to your account and check myorder <br> <a href='http://127.0.0.1:8000/User_login'>Login </a>"
        from_email = 'syamtechy5885@gmail.com'  # the sender's email address
        recipient_list =[usereml]  # list of recipient email addresses

        send_mail(subject, message, from_email, recipient_list)
        
        order_obj = OrderTrac.objects.select_related('orderid', 'userid').order_by('id').all()
        
        return render(request, 'orderTrac/admin_orderdetail.html', {'order': order_obj})
    
def postApprove(req):
    if req.GET.get('idn'):
        if req.method=="GET":
            try:
                postid=req.GET.get('idn')
                sts=req.GET.get('sts')
                obj=posts_tbl.objects.get(id=postid)
                if obj:
                    obj.approve=sts
                    obj.save()
                    post=posts_tbl.objects.select_related('user').filter(approve=False).order_by('-id')
                    post2=posts_tbl.objects.select_related('user').filter(approve=True).order_by('-id')
                    return render(req,"admin/Adminpostapprove.html",{'data':post,'data2':post2,'cmmt':""}) 
            except Exception as e:
                return HttpResponse(e)    
    else: 
        post=posts_tbl.objects.select_related('user').filter(approve=False).order_by('-id')
        post2=posts_tbl.objects.select_related('user').filter(approve=True).order_by('-id')
        comment=comments_tbl.objects.select_related('post').all()
        return render(req,"admin/Adminpostapprove.html",{'data':post,'data2':post2,'cmmt':""})    
cnt=True    
def CommentApprove(req):
    global cnt
    cmt=[]
    print('comment')
    if req.GET.get('pid'):
        print('pid')
        if req.method=="GET":
            try:
                postid=req.GET.get('pid')
                print(postid,'postid')
                obj=posts_tbl.objects.get(id=postid)
                              
                if obj:
                    # if cnt:
                        comment=comments_tbl.objects.select_related('post').filter(post=obj.id)
                        for  cm in comment:
                            # if cm.post.id in postid:
                                cmt.append(cm.comment)
                                print(cmt)
                        cnt=False        
                       
                    # else:
                    #     comment=""    
                    #     cnt=True

                        post=posts_tbl.objects.select_related('user').order_by('-id').filter(approve=False)
                        post2=posts_tbl.objects.select_related('user').order_by('-id').filter(approve=True)
                        return render(req,"admin/Adminpostapprove.html",{'data':post,'data2':post2,'cmmt':comment})  
            except Exception as e:
                return HttpResponse(e)    
    else: 
        post=posts_tbl.objects.all()
        return render(req,"admin/Adminpostapprove.html",{'data':post,'cmmt':""})    
    
def deletecomment(req):
    if req.GET.get('cmtid'):
        cmtid=req.GET.get('cmtid')
        obj=comments_tbl.objects.get(id=cmtid)
        obj.delete()
    return redirect("/postApprove")    
def viewContact(req):
    obj=Contact.objects.all()
    
    return render(req,'admin/viewcontact.html',{'data':obj})




    
         
    
    
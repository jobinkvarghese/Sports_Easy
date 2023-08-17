
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('',views.index),
    path('main',views.index),
    path('User_reg',views.User_reg),
    path('User_login',views.User_login),
    path('sports_items',views.sports_items),  
    path('add_to_cart',views.add_to_cart),
    path('cart_view',views.cart_view),
    path('remove_from_cart',views.remove_from_cart),
    path('booking',views.booking),
    path('Save_booking',views.Save_booking),
    path('payment',views.payment),
    path('my_order',views.orderDetail),
    path("orderCancel",views.orderCancel),
    # path('cancel_booking_sports_item',views.cancel_booking_sports_item),
    path('complaint_reg_view',views.complaint_reg_view),
    path('save_complaint',views.save_complaint),
    path('complaint_view',views.complaint_view),
    path('user_home_view',views.user_home_view),
    path('Event_view',views.Event_view),
     path('event_book',views.event_book),
    path('Event_pay_submit',views.Event_pay_submit),
    path('event_mybooking_view',views. event_mybooking_view),
    path("cancel_event",views.event_cancel),
    path('event_search',views.event_search),
    path('User_academy_view',views.User_academy_view),
    path('Admission_form_view',views. Admission_form_view),
    path('User_academy_admission',views.User_academy_admission),
    path('academy_search',views.academy_search),
    path('My_addmision_view',views.My_addmision_view),
    path('post_view',views.post_view),
    path('make_post',views.make_post),
    path('comment',views.comment),
    path('user_turf_view',views.user_turf_view),
    path('turf_book',views.turf_book),
    path('turf_pay',views.turf_pay),
    path('turf_my_booking',views.turf_my_booking),
    path('turf_cancel_book',views.turf_cancel_book),
    path('p_search',views.p_search),
    path('turf_search',views.turf_search),
    path('my_post_view',views.my_post_view),
    path('delete_post',views.delete_post),
    path('user_profile',views.user_profile),
    path('order_detail',views.orderDetail),
    path('nwcrtdelete',views.nwcrtdelete),
    path('newpayment',views.newpayment),
    path('pay',views.payM),
    path('placeorder',views.placeorder),
    path('userorderdetails',views.orderDetail),
    path('userorderdetail',views.orderView),
    path('user_logout',views.user_logout),
    path('discard',views.discard),
    path('usercontact', views.contact),
    path('contact_success',views.contact_success)

  
 
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
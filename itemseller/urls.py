from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    
    path('itemseller_reg',views.itemseller_reg),
    path('itemseller_login',views.itemseller_login),
    path('product_upload',views.product_upload),
    path('product_view',views.product_view),
    path('delete',views.delete),
    path('edit',views.edit),
    path('product_update',views.product_update),
    path('user_complaint_view',views.User_complaint_view),
    path('update_complaint',views.Update_complaint),
    path('solved_complaints',views.solved_complaint_view),
    path('itemseller_booking_view',views.itemseller_booking_view),
    path('item_booking_delivery',views.item_booking_delivery),
    path('delivered_products',views.delivered_products),
    path('home_view',views.home_view),
    path('logout_view',views.logout_view),
    path('itemseller_home_view',views.itemseller_home_view),
    path('createcategory',views.createCategory),
    path('productDelete',views.delete),
    path('seller_booking',views.orderView),
    
    


    
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
 
    path('Turf_reg',views.Turf_reg),
    path('Turf_login',views.Turf_login),
    path('slot_add',views.slot_add),
    path('turf_home',views.turf_home),
    path('slot_view',views.slot_view),
    path('slot_edit',views.slot_edit),
    path('turf_view_booking',views.turf_view_booking),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
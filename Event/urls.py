from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
 path('Event_reg_view',views.Event_reg_view),
 path('Event_reg',views.Event_reg),
 path('Event_login_view',views.Event_login_view),
 path('Event_manage_reg',views.Event_manage_reg),
 path('Event_manager_reg_view',views.Event_manager_reg_view),
 path('Event_manage_login',views. Event_manage_login),
 path('my_event_view',views.my_event_view),
 path('event_booking_view',views.event_booking_view),
 path('event_home',views.event_home),
 path('event_booking_table',views.event_booking_table),
 path('update_event',views.update_event),
 path("eventDelete",views.eventDelete),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
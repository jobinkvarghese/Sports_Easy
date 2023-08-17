from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
path('Academy_reg',views.Academy_reg),
path('Academy_login',views.Academy_login),
path('Academy_profile_view',views.Academy_profile_view),
path('Academy_update_view',views.Academy_update_view),
path('Academy_update',views.Academy_update),
path('Academy_home_view',views.Academy_home_view),
path('academy_booking_view',views.academy_booking_view),
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
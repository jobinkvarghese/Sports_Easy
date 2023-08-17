from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('User_reg',views.User_reg),
    path('User_login',views.User_login)
    
]

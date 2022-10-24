from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('login', views.loginuser, name='loginuser'),
   path('register', views.registeruser, name='registeruser'),
]
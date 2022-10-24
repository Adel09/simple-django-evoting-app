from django.urls import path
from . import views

urlpatterns = [
   path('home', views.dashboard_home, name='dashboard-home'),
   path('vote', views.cast_votes, name='cast-votes'),
   path('thanks', views.thanks, name='thanks')
]

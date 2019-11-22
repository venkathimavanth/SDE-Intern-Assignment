from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'management'

urlpatterns = [
    path('',views.Home,name='Home'),
    path('entry/',views.Entry,name='Entry'),
    path('exit/',views.Exit,name='Exit'),
    ]

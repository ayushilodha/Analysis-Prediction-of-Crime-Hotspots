from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("about/",views.about,name='about'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('view',views.view,name='view'),
    path('moduless',views.moduless,name='moduless'),
    path('prediction',views.prediction,name='prediction'),
    # path('result',views.result,name='result'),
]
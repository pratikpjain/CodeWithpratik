from django.contrib import admin
from django.urls import path
from CodeQuest import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('reset-password', views.reset_password, name='reset-password'),
    path('question', views.putQuestion, name = 'put-question')
]

from django.contrib import admin
from django.urls import path, include
from cwPratik import views

urlpatterns = [
    path("", views.index, name='code')
]

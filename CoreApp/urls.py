from django.contrib import admin
from django.urls import path
from CoreApp import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('extractImage',views.extractImage,name="extrect"),
]
from django.contrib import admin
from django.urls import path
from CoreApp import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('extractImage',views.extractImage,name="extrect"),
    path('audiolist',views.audioList,name="audio list"),
    path('PDFex',views.PDFPage,name="pdf extrect"),
]
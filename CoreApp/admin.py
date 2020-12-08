from django.contrib import admin

# Register your models here.
from CoreApp.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','imgs','language','title','res_img','content','songfile']
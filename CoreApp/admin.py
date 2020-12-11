from django.contrib import admin

# Register your models here.
from CoreApp.models import Image,PDF


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','imgs','language','title','res_img','content','songfile']
@admin.register(PDF)
class PDFAdmin(admin.ModelAdmin):
    list_display = ['id','pdf_file','language','img_folder','img_pinter','title','content','songfile']
from django import forms
from .models import Image,PDF
from .validators import validate_file_extension


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['imgs','language']
        labels={'imgs':'','language':'language'}
        widgets = {
            'language': forms.Select(attrs={'class': 'form-control mr-3',}),
        }

class PDFForm(forms.ModelForm):
    class Meta:
        model=PDF
        fields=['pdf_file','language','title']
        labels = {'pdf_file': '', 'language': 'language','title':'title'}
        widgets = {
            'language': forms.Select(attrs={'class': 'form-control mr-3', }),
        }


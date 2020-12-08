from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['imgs','language']
        labels={'imgs':'','language':'language'}
        widgets = {
            'language': forms.Select(attrs={'class': 'form-control mr-3',}),
        }
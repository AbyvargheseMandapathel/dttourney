from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *

class PostAdsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'title', 
        'placeholder': 'Title'
    }))

    description = forms.CharField(widget=CKEditorWidget(attrs={
        'type': 'text',
        'class': 'form-control',  
        'name': 'description', 
        'placeholder': 'Description'
    }))

    

    class Meta:
        model = Ads
        fields = '__all__'
        exclude = ['author', 'date_created', 'is_featured']

    

    
        
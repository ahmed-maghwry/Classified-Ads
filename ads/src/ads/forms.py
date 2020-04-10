from django import forms
from .models import ads , catugry
import PIL

class adsform(forms.ModelForm):
    class Meta:
        model = ads
        fields = ['title', 'description' , 'ad_option' , 'main' 
                , 'sub','end' ,'name_of_who','adress','mobile','email' ]



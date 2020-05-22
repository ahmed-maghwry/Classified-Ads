from django import forms
from ads.models import ads  , car_form
import PIL



class general(forms.ModelForm):
    
    class Meta:
        model = ads
        fields = [ 'title' , 'sub','end' , 'last'  ]


class car_search(forms.ModelForm):
    class Meta:
        model = car_form
        exclude = ['ad_id' ]


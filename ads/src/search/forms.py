from django import forms
from ads.models import ads  , car_form
import PIL



class general(forms.ModelForm):
    
    class Meta:
        model = ads
        fields = [  'sub','end' , 'last'  ]

class price_form (forms.Form):
    from_Price = forms.DecimalField(max_digits=14 , decimal_places=4 , label ='Price from')
    to_Price = forms.DecimalField(max_digits=14 , decimal_places=4 ,  label ='Price to')





class car_search(forms.ModelForm):
    class Meta:
        model = car_form
        exclude = ['ad_id' , 'Price' ]


from django import forms
from ads.models import  ads  ,car_form ,motorcycles , car_spare_parts , Boats ,heavy_trucks ,mobile_phones , mobile_accessories 
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

class motorcycles_search(forms.ModelForm):
    class Meta:
        model = motorcycles
        exclude = ['ad_id' , 'Price' ]

class car_spare_parts_search(forms.ModelForm):
    class Meta:
        model = car_spare_parts
        exclude = ['ad_id' , 'Price' ]

class Boats_search(forms.ModelForm):
    class Meta:
        model = Boats
        exclude = ['ad_id' , 'Price' ]

class heavy_trucks_search(forms.ModelForm):
    class Meta:
        model = heavy_trucks
        exclude = ['ad_id' , 'Price' ]

class mobile_phones_search(forms.ModelForm):
    class Meta:
        model = mobile_phones
        exclude = ['ad_id' , 'Price' ]

class mobile_accessories_search(forms.ModelForm):
    class Meta:
        model = mobile_accessories
        exclude = ['ad_id' , 'Price' ]


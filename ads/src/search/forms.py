from django import forms
from ads.models import  *
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
        model = db_car
        exclude = ['ad_id' , 'Price' ]

class motorcycles_search(forms.ModelForm):
    class Meta:
        model = db_motorcycles
        exclude = ['ad_id' , 'Price' ]

class car_spare_parts_search(forms.ModelForm):
    class Meta:
        model = db_car_spare_parts
        exclude = ['ad_id' , 'Price' ]

class Boats_search(forms.ModelForm):
    class Meta:
        model = db_Boats
        exclude = ['ad_id' , 'Price' ]

class heavy_trucks_search(forms.ModelForm):
    class Meta:
        model = db_heavy_trucks
        exclude = ['ad_id' , 'Price' ]

class mobile_phones_search(forms.ModelForm):
    class Meta:
        model = db_mobile_phones
        exclude = ['ad_id' , 'Price' ]

class mobile_accessories_search(forms.ModelForm):
    class Meta:
        model = db_mobile_accessories
        exclude = ['ad_id' , 'Price' ]


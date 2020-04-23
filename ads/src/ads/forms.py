from django import forms
from .models import ads , catugry , car_form
import PIL
from django.forms.widgets import RadioSelect

class car_forms(forms.ModelForm):

    class Meta:
        model = car_form
        exclude = ['ad_id']
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.BooleanField.widget.forms.update(RadioSelect)
            # .widget.attrs.update({'class': 'special'})
            # widget=forms.RadioSelect
            # self.fields['comment'].widget.attrs.update(size='40')
class carf(forms.ModelForm):
    class Meta:
        model = catugry
        fields = ['name', 'main'  ]
class mobilef(forms.ModelForm):
    class Meta:
        model = catugry
        fields = ['name','sub', 'end'  ]
class adsform(forms.ModelForm):
    class Meta:
        model = ads
        fields = ['title', 'description' , 'ad_option' , 'main' 
                , 'sub','end' , 'last' , 'img','name_of_who','adress','mobile','email' ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub'].queryset = catugry.objects.none()
        self.fields['end'].queryset = catugry.objects.none()
        self.fields['last'].queryset = catugry.objects.none()
        # self.fields['last'].widget = forms.HiddenInput()
        if 'main' in self.data:
            try:
                main_id = int(self.data.get('main'))
                self.fields['sub'].queryset = catugry.objects.filter(main_id=main_id , sub_id=None).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub'].queryset = self.instance.main.sub_set.order_by('name')   
#################################################################
        if 'sub' in self.data:
            try:
                sub_id = int(self.data.get('sub'))
                self.fields['end'].queryset = catugry.objects.filter(main_id=main_id ,sub_id=sub_id ,end_id=None).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['end'].queryset = self.instance.main.sub.end_set.order_by('name')   
#################################################################
        if 'end' in self.data:
            try:
                end_id = int(self.data.get('end'))
                self.fields['last'].queryset = catugry.objects.filter(main_id=main_id ,sub_id=sub_id ,end_id=end_id ).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['last'].queryset = self.instance.main.sub.end_set.order_by('name')


        
         





from django import forms
from .models import ads , catugry
import PIL

class adsform(forms.ModelForm):
    class Meta:
        model = ads
        fields = ['title', 'description' , 'ad_option' , 'main' 
                , 'sub','end' , 'img','name_of_who','adress','mobile','email' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub'].queryset = catugry.objects.none()
        self.fields['end'].queryset = catugry.objects.none()
        if 'main' in self.data:
            try:
                main_id = int(self.data.get('main'))
                self.fields['sub'].queryset = catugry.objects.filter(main_id=main_id , sub_id=None).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['sub'].queryset = self.instance.main.sub_set.order_by('name')    





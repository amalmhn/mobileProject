from django import forms

from .models import MobileModel
from django.forms import ModelForm, Textarea , TextInput



class MobileCreateForm(ModelForm):
    class Meta:
        model = MobileModel
        fields = '__all__'
        widgets = {
             'phone_name' : forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'memory': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        memory = cleaned_data.get('memory')
        price = cleaned_data.get('price')
        if memory<16:
            msg = 'Invalid Entry'
            self.add_error('memory',msg)
        if price<1:
            msg = 'Invalid Entry'
            self.add_error('price',msg)
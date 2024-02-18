from .models import Shed
from django.forms import ModelForm, TextInput


class ShedForm(ModelForm):
    class Meta:
        model = Shed
        fields = ['name', 'kolvo', 'price']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название товара'
            }),
            "kolvo": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Кол-во'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            })
        }
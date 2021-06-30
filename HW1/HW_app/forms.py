from django import forms
from django.forms import TextInput, NumberInput, Select

from HW_app.models import Product, Review


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = 'title description price category'.split()
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Название товара'
                }
            ),
            'description': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Описание товара'
                }
            ),
            'price': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Цена'
                }
            ),
            'category': Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = 'product text'.split()
        widgets = {
            'product': Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'text': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите отзыв'
                }
            )
        }

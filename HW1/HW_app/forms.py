from django import forms
from django.core.exceptions import ValidationError
from django.forms import TextInput, NumberInput, Select

from HW_app.models import Product, Review
from django.contrib.auth.models import User


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
            ),
        }


class UserRegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Email',
            'class': 'form-control'
        }
    ))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Пароль',
                                          'class': 'form-control'}
                               ))
    password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Подтвердите пароль',
                                           'class': 'form-control'}
                                ))

    def clean_email(self):
        users = User.objects.filter(username=self.cleaned_data['email'])
        if users.count() > 0:
            raise ValidationError('Эта почта уже используется')

    def clean_password(self):
        p_wrd = self.cleaned_data.get('password', '')
        p_wrd1 = self.cleaned_data.get('password1', '')
        if p_wrd != p_wrd1:
            raise forms.ValidationError('Пароли не совпадают')


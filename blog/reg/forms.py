from .models import user
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(ModelForm):
    class Meta:
        model = user
        fields = ['username', 'password']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            }),
        }
#from .models import Artiles
from django.forms import ModelForm, TextInput
from django.contrib.auth.models import User

class SearchForm(ModelForm):
    class Meta:
        #model = Artiles

        fields = ['search']
        widgets = {
            'search': TextInput(attrs={
                'class': 'form-control me-2',
                'type': 'search',
                'placeholder': "Поиск",
            }),
        }
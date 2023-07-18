from django.shortcuts import render,redirect
from . import forms
from .models import user
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm

def register(request):
    data = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = "Всё прошло успешно"
            return redirect('..')
    else:
        form = UserCreationForm()
        data['form'] = form
        return render(request, 'reg/reg.html', data)
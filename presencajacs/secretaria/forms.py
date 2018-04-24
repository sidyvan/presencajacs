from django import forms
from django.forms import TextInput,Select , Textarea, PasswordInput, EmailField
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'name':'username'}),
            'password': PasswordInput(attrs={'class': 'form-control', 'name':'password'}),

        }


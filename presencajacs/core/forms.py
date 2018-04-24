from django import forms
from core.models import Presenca
from django.forms import TextInput,Select , Textarea, PasswordInput, EmailField





class PresencaForm(forms.ModelForm):
    class Meta:
        model = Presenca
        fields = ('ra', )

        widgets = {

            'ra': TextInput(attrs={'class': 'form-control', 'name':'ra', 'autofocus':'autofocus', 'maxlength':'6','minlength':'6' }),

        }

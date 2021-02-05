from django import forms
from .models import DocInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm, forms.Form):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        username = forms.CharField(max_length=200)
        password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput())
        password2 = forms.CharField(label="Confirme", widget=forms.PasswordInput())

class Docs(forms.ModelForm):
    class Meta:
        model = DocInfo
        fields = ['NombreDrDra','LastName','asignatura','ciclo', 'carrera']

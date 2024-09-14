from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}),label='Nombre de usuario')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label='Ingrese Contraseña'
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label='Vuelva a escribir la contraseña'
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )

class loginForm(forms.Form):

    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}),label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Contraseña')
    
    class Meta:
        model = User
        fields = ('username', 'password',)

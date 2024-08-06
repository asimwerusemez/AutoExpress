from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Entre votre Nom d'utilisateur"}), label='')

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Entre votre Nom de la famille"}), label='')

    telephone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Entre votre Télephone"}), label='')
    
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Entre votre Email"}), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Créer un Mot de passe"}), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirmation mot de passe"}), label='')


    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "telephone",
            "email",
            "password1",
            "password2",
        )



class ConnexionForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'votre-classe-css', 
        'placeholder': "Nom d'utilisateur", 
    }), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'votre-classe-css',
        'placeholder': 'Mot de passe', 
    }), label='')

    class Meta:
        model = User
        fields = ('username', 'password')


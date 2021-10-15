from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.forms import PasswordInput

class RegisterUserForm(UserCreationForm):

    username=forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class':'form-control'}))
    first_name=forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First name', 'class':'form-control'}))
    last_name=forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class':'form-control'}))
    email=forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email address', 'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
   
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Create password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat password'})
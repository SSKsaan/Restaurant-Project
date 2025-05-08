from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email')

class EmailChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email',)
    username = forms.CharField(disabled=True)
    password = None

class PassChangeForm(PasswordChangeForm):
    new_password2 = None
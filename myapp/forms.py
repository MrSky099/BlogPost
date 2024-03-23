from django import forms
from myapp.models import User

class UserForm(forms.ModelForm):
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ['Firstname', 'Lastname', 'Username', 'email', 'Phone_Number', 'password', 'password2']


class LoginForm(forms.Form):
    Username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
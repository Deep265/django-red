from django import forms
from . import models

class User_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','label':''}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone number,username or email','label':''}))
    class Meta():
        model = models.User_info
        fields =('username','password')
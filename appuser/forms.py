from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm (UserCreationForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.fields ['username'].widget.attrs.update({
            'required': '',
            'placeholder':'Username',
            'type':'text',
            'aria-label':'username',
            'class':'form-control form-control-lg w-100 username'
        })
        self.fields ['first_name'].widget.attrs.update({
            'required': '',
            'placeholder':'First name',
            'type':'text',
            'aria-label':'first-name',
            'class':'form-control form-control-lg w-100 first-name'
        })
        self.fields ['last_name'].widget.attrs.update({
            'required': '',
            'placeholder':'Last name',
            'type':'text',
            'aria-label':'last-name',
            'class':'form-control form-control-lg w-100 last-name'
        })
        self.fields ['email'].widget.attrs.update({
            'required': '',
            'placeholder':'Email',
            'type':'email',
            'aria-label':'email',
            'class':'form-control form-control-lg w-100 email'
        })
        self.fields ['password1'].widget.attrs.update({
            'required': '',
            'placeholder':'Password',
            'type':'password',
            'aria-label':'password',
            'class':'password-input form-control form-control-lg'
        })
        self.fields ['password2'].widget.attrs.update({
            'required': '',
            'placeholder':'Confirm Password',
            'type':'password',
            'aria-label':'password',
            'class':'password-input form-control form-control-lg'
        })

    email = forms.EmailField()

    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        

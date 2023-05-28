from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm (UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        self.fields ['first_name'].widget.attrs.update({
            'required': '',
            'placeholder':'First name',
            'type':'text',
            'id':'validationServer01',
            'aria-label':'first-name',
            'aria-describedby':'basic-addon1',
            'class':'form-control form-control-lg w-100 first-name'
        })
        self.fields ['last_name'].widget.attrs.update({
            'required': '',
            'placeholder':'Last name',
            'type':'text',
            'id':'validationServer02',
            'aria-label':'last-name',
            'aria-describedby':'basic-addon2',
            'class':'form-control form-control-lg w-100 last-name'
        })
        self.fields ['email'].widget.attrs.update({
            'required': '',
            'placeholder':'Email',
            'type':'email',
            'id':'validationServer03',
            'aria-label':'email',
            'aria-describedby':'basic-addon3',
            'class':'form-control form-control-lg w-100 email'
        })
        self.fields ['password1'].widget.attrs.update({
            'required': '',
            'placeholder':'Password',
            'type':'password',
            'id':'validationServer05',
            'aria-label':'password',
            'aria-describedby':'basic-addon5',
            'class':'password-input form-control form-control-lg'
        })
        self.fields ['password2'].widget.attrs.update({
            'required': '',
            'placeholder':'Confirm Password',
            'type':'password',
            'id':'validationServer05',
            'aria-label':'password',
            'aria-describedby':'basic-addon5',
            'class':'password-input form-control form-control-lg'
        })
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        

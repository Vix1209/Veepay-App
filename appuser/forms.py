from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


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
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("That username is already taken, Please try registering by a different username")
    
    
    
# class loginForm(AuthenticationForm):

        
#     # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg w-100 username', 'required': '', 'placeholder':'Username', 'type':'text', 'aria-label':'Username', 'id': 'validationServer03'}))
#     # password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class':'password-input form-control form-control-lg', 'required': '', 'placeholder':'Password', 'type':'password', 'aria-label':'password',}))
    
#     class Meta:
#         model = User,
#         fields = ('username', 'password')

    
    
class UserUpdateForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name']
        

class ProfileUpdateForm (forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'image']
        

# class OtpForm (forms.ModelForm):
    
        

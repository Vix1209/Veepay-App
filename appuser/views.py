from django.shortcuts import render, redirect
from .forms import SignUpForm, UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    # return HttpResponse('this is the login page')
    redirect ('login_successful')
    return render(request, 'user/login.html')

def login_successful(request):
    # return HttpResponse('this is the login_successful page')
    return render(request, 'user/Login_successful.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            
            form.save()
            new_user = authenticate(first_name = first_name, last_name = last_name, email = email, password = password)
            if new_user is not None:
                login(request, new_user)
                return redirect ('index')
            
    else:        
        form = SignUpForm()
        
    context = {
        'form': form
    }
    return render(request, 'user/signup.html', context)

def signup_successful(request):
    # return HttpResponse('this is the signup_successful page')
    return render(request, 'user/Signup_successful.html')

def reset_password(request):
    # return HttpResponse('this is the reset_password page')
    return render(request, 'user/forget-password1.html')

def OTP(request):
    # return HttpResponse('this is the OTP page')
    return render(request, 'user/forget-password2.html')

def change_password(request):
    # return HttpResponse('this is the change_password page')
    return render(request, 'user/forget-password3.html')

def enter_new_login_details(request):
    # return HttpResponse('this is the change_password page')
    return render(request, 'user/forget-password4.html')


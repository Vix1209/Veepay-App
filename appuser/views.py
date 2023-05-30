from django.shortcuts import render, redirect
from .forms import SignUpForm
# from django.contrib.auth import authenticate, login

# Create your views here.

def signup(request):
    if request.method == "POST":
        print ('success')

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print ('success')

            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')            

            # User = authenticate(username = username, password = password)    
            # login(request, User)
            return redirect('signup_successful')
    
    else:        
        form = SignUpForm()
        print('denied')
        
    context = {
        'form': form
    }
    return render(request, 'user/signup.html', context)

def signup_successful(request):
    # return HttpResponse('this is the signup_successful page')
    return render(request, 'user/Signup_successful.html')

def login(request): 
    # return HttpResponse('this is the login page')
    # redirect ('login_successful')
    return render(request, 'user/login.html')

def login_successful(request):
    # return HttpResponse('this is the login_successful page')
    return render(request, 'user/Login_successful.html')

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


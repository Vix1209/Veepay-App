from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    # return HttpResponse('this is the login page')
    return render(request, 'user/Login.html')

def login_successful(request):
    # return HttpResponse('this is the login_successful page')
    return render(request, 'user/Login_successful.html')

def login_error(request):
    # return HttpResponse('this is the login_error page')
    return render(request, 'user/Login_error.html')

def signup(request):
    # return HttpResponse('this is the signup page')
    return render(request, 'user/signup.html')

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


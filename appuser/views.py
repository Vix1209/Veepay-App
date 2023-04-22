from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return HttpResponse('this is the login page')

def login_successful(request):
    return HttpResponse('this is the login_successful page')

def login_error(request):
    return HttpResponse('this is the login_error page')

def signup(request):
    return HttpResponse('this is the signup page')

def signup_successful(request):
    return HttpResponse('this is the signup_successful page')

def reset_password(request):
    return HttpResponse('this is the reset_password page')

def OTP(request):
    return HttpResponse('this is the OTP page')

def change_password(request):
    return HttpResponse('this is the change_password page')


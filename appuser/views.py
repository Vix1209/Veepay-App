from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    # return HttpResponse('this is the login page')
    redirect ('login_successful')
    return render(request, 'user/login.html')

def login_successful(request):
    # return HttpResponse('this is the login_successful page')
    return render(request, 'user/Login_successful.html')

def signup(request):
    # if request.method == 'POST':
    #     form =  forms.CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         staff_name = form.cleaned_data.get('username')
    #         message = messages.success (request, f'New account successfully created for "{staff_name}", Proceed to login')
    #         return redirect('user-login')
    # else:
    #     form =  forms.CreateUserForm()
        
    # context = {
    #     'form': form,
    # }
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

def enter_new_login_details(request):
    # return HttpResponse('this is the change_password page')
    return render(request, 'user/forget-password4.html')


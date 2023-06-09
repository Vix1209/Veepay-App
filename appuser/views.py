from django.shortcuts import  render, redirect
from .forms import SignUpForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(request):
    if request.method == "POST":
        
        #making use of the default UserCreationForm that django provides. For this, have the attributes, attached to the input form, accurately placed in order as it is in the forms.py file in appuser app
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print ('account created')

        ## without using django default form. This way, you parse the form having an inpt tag, normally as you would do it on the frontend. but you attach a name attribute which will be made use of over here.
        # username = request.POST['signup-username']
        # firstname = request.POST['signup-firstname']
        # lastname = request.POST['signup-lastname']
        # email_address = request.POST['signup-email']
        # p1 = request.POST['signup-p1']
        # p2 = request.POST['signup-p2']
        
        ## the variables above will have the particular names it's grabbing data from, to be the exact same as each input tag form on the frontend.
        
        # user = User.objects.create(username, email_address, p1)
        # user.first_name = firstname
        # user.last_name = lastname
        # user.save()
        # return redirect ('signup_successful')
               
            ##registration successful email
            email = form.cleaned_data.get ('email')
            subject, from_email, to = 'Registration Successful!', 'VEEPAY <veepay.ng@gmail.com>', email
            text_content = loader.render_to_string('user/email_auth.txt')
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.content_subtype = 'html'
            msg.send()    
            print ('email sent')
            message = messages.success(request, "Registration successful." )

            return redirect('signup_successful')
        message = messages.error(request, "Unsuccessful registration. Invalid information.")
                  
    else:
        form = SignUpForm()
        
    context = {
        'form': form,
    }
    return render(request, 'user/signup.html', context)


def signup_successful(request):
    return render(request, 'user/Signup_successful.html')


def login(request): 
    if request.method == 'POST':
        user_name = request.POST['login-username']
        user_password = request.POST['login-password']
        user = authenticate(username = user_name, password = user_password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('login_successful')
        else:
            messages.error(request, f'Account does not exist')  

    return render(request, 'user/login.html')



def login_successful(request):
    # return HttpResponse('this is the login_successful page')
    return render(request, 'user/Login_successful.html')


def logout (request):
    auth_logout(request)
    messages.success(request, 'logout successful')
    return render (request, 'user/logout.html')


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


@login_required
def settings(request):
    return render(request, 'user/settings.html')
    # return HttpResponse('this is the settings page')
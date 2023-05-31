from django.shortcuts import  render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
# from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.template import loader

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print ('account created')

            ##registration successful email
            email = form.cleaned_data.get ('email')
            subject, from_email, to = 'Registration Successful 🎇', 'VEEPAY <veepay.ng@gmail.com>', email
            text_content = loader.render_to_string('user/email_auth.txt')
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.content_subtype = 'html'
            msg.send()    
            print ('email sent')
            messages.success(request, "Registration successful." )

            return redirect('signup_successful')
        messages.error(request, "Unsuccessful registration. Invalid information.")

          
    else:
        form = SignUpForm()
        print('denied')
        
    context = {
        'form': form,
     
    }
    return render(request, 'user/signup.html', context)



def signup_successful(request):
    # return HttpResponse('this is the signup_successful page')
    return render(request, 'user/Signup_successful.html')

def login(request): 
    if request.method == 'POST':
      
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('login_successful')
        else:
            messages.info(request, f'account done not exit plz sign in')
    
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'user/login.html', context)


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


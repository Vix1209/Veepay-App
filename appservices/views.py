from django.shortcuts import render, redirect
# from django.http import HttpResponse, 
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from .models import Newsletter


# Create your views here.
def index(request):
    
    
    ## newsletter
    if request.method == 'POST':
        
        email = request.POST['user_email']
        subscribe = Newsletter(email = email)
        subscribe.save()
        
        #sending the email
        subject, from_email, to = "Welcome To VEEPAY Telecom 💙", "VEEPAY <veepay.ng@gmail.com>", email 
        text_content = loader.render_to_string('newsletter/contact_form.txt')  
              
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        
        # this converts the text to html 
        msg.content_subtype = 'html'
        
        msg.send()
              
        # message to be printed out on the terminal       
        print( 'Subscription Successful')
        
        # where to redirect to after sending mail
        return redirect ('success/')
    
    ##newsletter ends
    return render(request, 'services/index.html')

@login_required
def cable (request):
    return render(request, 'services/Cable tv subscription.html')
    # return HttpResponse('this is the cable page')

@login_required
def bulk_sms (request):
    return render(request, 'services/Bulk SMS.html')
    # return HttpResponse('this is the cable page')

@login_required
def airtime(request):
    return render(request, 'services/Buy Airtime.html')
    # return HttpResponse('this is the airtime page')

@login_required
def SME(request):
    return render(request, 'services/BUY SME DATA.html')
    # return HttpResponse('this is the SME page')

@login_required
def fund(request):
    return render(request, 'services/funds.html')
    # return HttpResponse('this is the fund page')
    
    
@login_required
def payment_declined(request):
    return render(request, 'services/Payment Declined.html')
    # return HttpResponse('this is the payment_declined page')

@login_required
def payment_successful(request):
    return render(request, 'services/Payment successful.html')
    # return HttpResponse('this is the payment_successful page')

@login_required
def recharge_successful(request):
    return render(request, 'services/Recharge successful.html')
    # return HttpResponse('this is the recharge_successful page')

@login_required
def recharge_unsuccessful(request):
    return render(request, 'services/Recharge Unsuccessful.html')
    # return HttpResponse('this is the recharge_unsuccessful page')

def selltous_intro(request):
    return render(request, 'services/selltous-intro.html')
    # return HttpResponse('this is the selltous_intro page')

@login_required
def selltous(request):
    return render(request, 'services/selltous.html')
    # return HttpResponse('this is the selltous page')

@login_required
def withdraw(request):
    return render(request, 'services/withdraw.html')
    # return HttpResponse('this is the withdraw page')

def settings(request):
    return render(request, 'services/settings.html')
    # return HttpResponse('this is the settings page')

def about(request):
    return render(request, 'services/aboutus.html')
    # return HttpResponse('this is the settings page')


def thanks(request):
    return render(request, 'newsletter/thankyou.html')
from django.shortcuts import render
# from django.http import HttpResponse, 

# Create your views here.

def index(request):
    return render(request, 'services/index.html')
    # return HttpResponse('this is the dashboard page')

def cable (request):
    return render(request, 'services/Cable tv subscription.html')
    # return HttpResponse('this is the cable page')

def bulk_sms (request):
    return render(request, 'services/Bulk SMS.html')
    # return HttpResponse('this is the cable page')

def airtime(request):
    return render(request, 'services/Buy Airtime.html')
    # return HttpResponse('this is the airtime page')

def SME(request):
    return render(request, 'services/BUY SME DATA.html')
    # return HttpResponse('this is the SME page')

def fund(request):
    return render(request, 'services/funds.html')
    # return HttpResponse('this is the fund page')

def payment_declined(request):
    return render(request, 'services/Payment Declined.html')
    # return HttpResponse('this is the payment_declined page')

def payment_successful(request):
    return render(request, 'services/Payment successful.html')
    # return HttpResponse('this is the payment_successful page')

def recharge_successful(request):
    return render(request, 'services/Recharge successful.html')
    # return HttpResponse('this is the recharge_successful page')

def recharge_unsuccessful(request):
    return render(request, 'services/Recharge Unsuccessful.html')
    # return HttpResponse('this is the recharge_unsuccessful page')

def selltous_intro(request):
    return render(request, 'services/selltous-intro.html')
    # return HttpResponse('this is the selltous_intro page')

def selltous(request):
    return render(request, 'services/selltous.html')
    # return HttpResponse('this is the selltous page')

def withdraw(request):
    return render(request, 'services/withdraw.html')
    # return HttpResponse('this is the withdraw page')

def settings(request):
    return render(request, 'services/settings.html')
    # return HttpResponse('this is the settings page')


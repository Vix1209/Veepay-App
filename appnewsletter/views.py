from django.shortcuts import render, HttpResponse

# Create your views here.
def email(request):
    return render(request, 'newsletter/email.html')
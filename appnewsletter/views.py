from django.shortcuts import render, HttpResponse

# Create your views here.
def email(request):
    return HttpResponse('this is the newsletter section')
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from .models import Newsletter
# from django_pandas.io import read_frame ##to be used when tryna send bulk messages



# Create your views here.



## TEMPLATE MAIL

def index(request):
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
    
    return render(request, 'newsletter/index.html')
    
   
   
   
   
##sending mass message to all subscribers... still needs work
   
# def index(request):
#     emails = Newsletter.objects.all()
#     df = read_frame(emails, filednames = ['email'])

#     mail_list = df['email'].values.tolist()

#     print (mail_list)

#     if request.method == 'POST':
        
#         email = request.POST['user_email']
#         subscribe = Newsletter(email = email)
#         subscribe.save()
            
            
            
#         subject, from_email, to = "Welcome To VEEPAY Telecom 💙", "VEEPAY <veepay.ng@gmail.com>", email 
#         text_content = loader.render_to_string('newsletter/contact_form.txt')  
              
#         msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        
#         # this converts the text to html 
#         msg.content_subtype = 'html'
        
#         msg.send()
      
#         # message to be printed out on the terminal       
#         print( 'Subscription Successful')
        
#         # where to redirect to after sending mail
#         return redirect ('success/')
    
#     return render(request, 'newsletter/index.html')

   
def about(request):
    return render(request, 'newsletter/aboutus.html')


def thanks(request):
    return render(request, 'newsletter/thankyou.html')
   
   

   
   
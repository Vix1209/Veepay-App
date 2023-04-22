from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    
    path('login_successful/', views.login_successful, name='login_successful'),
    
    path('login_error/', views.login_error, name='login_error'),
    
    path('signup/', views.signup, name='signup'),
    
    path('signup_successful/', views.signup_successful, name='signup_successful'),
    
    path('reset_password/', views.reset_password, name='reset_password'),
    
    path('OTP/', views.OTP, name='OTP'),
    
    path('change_password/', views.change_password, name='change_password'),
        
]

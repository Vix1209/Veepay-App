from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html') , name='login'),
    
    path('login_successful/', views.login_successful, name='login_successful'),
        
    path('signup/', views.signup, name='signup'),
    
    path('signup_successful/', views.signup_successful, name='signup_successful'),
    
    path('reset_password/', views.reset_password, name='reset_password'),
    
    path('OTP/', views.OTP, name='OTP'),
    
    path('change_password/', views.change_password, name='change_password'),
        
    path('reset_successful/', views.enter_new_login_details, name='enter_new_login_details'),
        
]

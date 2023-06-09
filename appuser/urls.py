from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
        # logic exist in the view. For customization, it will have a class in forms.py
    path('signup/', views.signup, name='signup'),

    path('signup_successful/', views.signup_successful, name='signup_successful'),
    
    
        # this have django default auth view
    path('login/', views.login, name='login'),

    path('login_successful/', views.login_successful, name='login_successful'),

    # path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name= 'logout'),
    path('logout/', views.logout, name = 'logout'),
  
  
        # password reset    
    path('reset_password/', views.reset_password, name='reset_password'),
    
    path('OTP/', views.OTP, name='OTP'),
    
    path('change_password/', views.change_password, name='change_password'),
        
    path('reset_successful/', views.enter_new_login_details, name='enter_new_login_details'),
 
    path('settings/', views.settings, name='settings'),
       
] 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('cable/', views.cable, name='cable'),
    
    path('airtime/', views.airtime, name='airtime'),
    
    path('SME/', views.SME, name='SME'),
    
    path('fund/', views.fund, name='fund'),
    
    path('payment_declined/', views.payment_declined, name='payment_declined'),
    
    path('payment_successful/', views.payment_successful, name='payment_successful'),
    
    path('recharge_successful/', views.recharge_successful, name='recharge_successful'),
    
    path('recharge_unsuccessful', views.recharge_unsuccessful, name='recharge_unsuccessful'),
    
    path('selltous_intro/', views.selltous_intro, name='selltous_intro'),
    
    path('selltous/', views.selltous, name='selltous'),
    
    path('withdraw/', views.withdraw, name='withdraw'),
    
    path('settings/', views.settings, name='settings'),
]

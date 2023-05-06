from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'newsletter_home'),
    path('about/', views.about, name = 'newsletter_about'),
    path('success/', views.thanks, name = 'newsletter_thanks'),
]

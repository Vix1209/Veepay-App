"""
URL configuration for telecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.templatetags.static import static # Not from django.conf.urls.static 
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView

# path('20220607_140201.png', RedirectView.as_view(url=staticfiles_storage.url('images/20220607_140201.png')))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appservices.urls')),
    path('accounts/', include('appuser.urls')),
    path('20220607_140201.jpg', RedirectView.as_view(url=static('20220607_140201.jpg'))),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




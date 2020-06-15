"""petproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from accounts.views import startpage, register, regi_profile, myprofile, login, photoplus, profileinform, home, lat_lon, matching, map_home, first, second, third
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/home/', home, name="home"),
    path('',startpage, name="startpage"),
    path('accounts/register/', register, name="register"),
    path('accounts/regi_profile/', regi_profile, name="regi_profile"),
    path('accounts/login/', LoginView.as_view(), name="login"),
    path('accounts/myprofile/', myprofile, name="myprofile"),
    path('accounts/photoplus/', photoplus, name="photoplus"),
    path('accounts/profileinform/', profileinform, name="profileinform"),
    path('lat_lon/', lat_lon, name="lat_lon"),
    path('accounts/matching/', matching, name="matching"),
    path('accounts/map_home/', map_home, name="map_home"),
    path('accounts/first/', first, name="first"),
    path('accounts/second/', second, name="second"),
    path('accounts/third/', third, name="third"),

] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

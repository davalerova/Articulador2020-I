"""IEEE_ETITC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from bases.views import Home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path( '', Home.as_view(), name='home' ),
    path('login/',auth_views.LoginView.as_view(template_name='bases/login.html'),
        name='login'),
    path('recuperar/',auth_views.LoginView.as_view(template_name='bases/recuperar.html'),
    name='recuperar'),
    path( 'logout/',
        auth_views.LogoutView.as_view( template_name='bases/home.html' ),
        name='logout' ),
        path('construccion/',auth_views.LoginView.as_view(template_name='bases/construccion.html'),
    name='construccion'),
    path('detalle/',auth_views.LoginView.as_view(template_name='bases/detalle.html'),
    name='detalle'),
]
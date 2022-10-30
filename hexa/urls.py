"""hexa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from setup.views import welcome
from setup.docs.user.user import login, register

urlpatterns = [
    path('', welcome),
    path('admin', admin.site.urls),
    path('login/', login, name='login'),
    path('register/', register, name='register'),

    path('api/method/setup/', include("setup.urls")), # setup
    path('api/method/account/', include("accounting.urls")), # accounting
    path('api/method/stock/', include("stock.urls")), # stock
    path('api/method/buying/', include("buying.urls")), # buying
    path('api/method/hr/', include("hr.urls")), # HR
    path('api/method/selling/', include("selling.urls")), # selling

    path('api/method/controller/', include("controller.urls")), # controllers

]

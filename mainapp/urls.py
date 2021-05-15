"""mainproject URL Configuration

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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('care', views.care, name='care'),
    path('codes', views.codes, name='codes'),
    path('contact', views.contact, name='contact'),
    path('faqs', views.faqs, name='faqs'),
    path('hold', views.hold, name='hold'),
    path('kitchen', views.kitchen, name='kitchen'),
    path('login', views.login, name='login'),
    path('offer', views.offer, name='offer'),
    path('register', views.register, name='register'),
    path('shipping', views.shipping, name='shipping'),
    path('single', views.single, name='single'),
    path('terms', views.terms, name='terms'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('logout', views.logout, name='logout')
]

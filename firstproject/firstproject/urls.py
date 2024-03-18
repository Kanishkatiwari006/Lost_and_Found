"""
URL configuration for firstproject project.

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
from django.urls import path
from firstApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('get_in_touch',views.get_in_touch),
    path('login/',views.login),
    path('register/',views.register),
    path('after_login/',views.after_login),
    path('item/',views.item),
    path('products/', views.Lost, name='Lost'),
    path('found/', views.Found, name='Found'),
    path('after_found/', views.after_found,name='after_found'),
    path('products/',views.products),
    path('after_products/', views.after_products, name='after_products'),
    path('after_products/claim',views.claim,name='claim'),
    path('logout/', views.logout, name='logout'),
]
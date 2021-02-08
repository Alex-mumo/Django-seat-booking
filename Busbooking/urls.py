from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include 
from App import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")), #authentication system
    path('register/', views.register, name = 'register'),
    path('base/', views.base, name = 'base'),
    path('home/', views.home, name = 'home'),
    path('logout/', views.LogOut, name = 'logout'),
    path('login/', views.LogIn, name = 'login'),
    path('contact/', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('findbus/', views.findbus, name = 'findbus'),
    path('show/', views.show, name='show'),
]

#django

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as main_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='main-login'),
    path('reg/', main_views.reg, name='registration'),
    path('home/',main_views.home,name='home')
]


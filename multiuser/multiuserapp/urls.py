from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_registration_view/', views.user_registration_view, name='user_registration'),
    path('dealer_registration_view/', views.dealer_registration_view, name='dealer_registration'),
    path('user_home/', views.user_home, name='user_home'),
    path('dealer_home/', views.dealer_home, name='dealer_home'),
    path('login_view/', views.login_view, name='login'),
]

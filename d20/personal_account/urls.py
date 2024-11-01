from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.user_account, name='account'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='personal_account/login.html'), name='login'),
    path('logout/', views.logout_account, name='logout'),
]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.get_candidatos, name='get_all_candidatos'),
    path('user/<int:cpf>',views.get_by_cpf),
    path('data/', views.candidato_manager),
    path('inserir/', views.inserir_candidato, name='inserir_candidato'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]

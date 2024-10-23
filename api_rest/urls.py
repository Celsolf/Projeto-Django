from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_candidatos, name='get_all_candidatos'),
    path('user/<int:cpf>',views.get_by_cpf),
    path('data/', views.candidato_manager)
]

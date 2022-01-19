from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('dashboard/relatorios/', views.RelatoriosView, name='relatorios'),
    path('dashboard/servicos/', views.ServicesView, name='servicos'),
    path('dashboard/carro/', views.CarroView, name='carro'),
    path('dashboard/configuracoes/', views.ConfigView, name='configuracoes'),
    path('dashboard/agendamentos/', views.AgendarView, name='agendamentos'),
]

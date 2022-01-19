from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Servicos, Agendamento


@login_required(login_url='login')
def DashboardView(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'dashboard.html')


def RelatoriosView(request):
    return render(request, 'relatorios.html')


def ServicesView(request):
    services = Servicos.objects.all()
    context = {'services': services}
    for e in services:
        print(e.nome)
    return render(request, 'servicos.html', context)


def CarroView(request):
    return render(request, 'carro.html')


def ConfigView(request):
    return render(request, 'configuracoes.html')


def AgendarView(request):
    agendamentos = Agendamento.objects.all()
    # queryset = Agendamento.objects.filter(pk=id)
    context = {'agendamentos': agendamentos}
    for e in agendamentos:
        print(e.placa)
    return render(request, 'agendamentos.html', context)

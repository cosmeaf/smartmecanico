from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from proposal.models import Proposta


@login_required(redirect_field_name='redirect_to')
def proposta(request, id=None, *args, **kwargs):
    error = get_object_or_404(Proposta, id=id)
    propostas = Proposta.objects.get(pk=id)
    print(propostas.cliente.username)
    print(propostas.cliente)
    print(propostas.data)
    context = {'proppostas': propostas, 'error': error}
    return render(request, 'proposta.html', context)

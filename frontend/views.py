from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def IndexFrontend(request):
    if not request.user.is_authenticated:
        return redirect(request, 'IndexFrontend')
    else:
        return render(request, 'proposta.html')

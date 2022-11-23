from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

from django.contrib.auth.decorators import login_required
def formula(request):
    titulo = 'Fórmula Médica'
    context = {
        'titulo': titulo 
    }
    return render(request, 'formula/formula.html', context)
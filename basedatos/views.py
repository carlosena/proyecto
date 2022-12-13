from django.shortcuts import render, redirect
import sys
from django.core.management import call_command
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def basedatos(request):
    titulo = 'Base Datos'
    context = {
        'titulo': titulo
    }
    
    return render(request, 'basedatos/base-datos.html', context)


@login_required
def respaldarbd(request):
    sysout = sys.stdout
    sys.stdout = open('db.json','w',1,'utf-8')    
    call_command('dumpdata')    
    sys.stdout = sysout    
    messages.success(request, 'Se respaldó la base de datos')
    #return HttpResponse("Hola desde respaldar")
    
    return redirect('basedatos')
  

@login_required
def recuperarbd(request):
    call_command('loaddata', 'db.json')
    messages.success(request, 'Se recuperó la base de datos')
    return redirect('basedatos')
    
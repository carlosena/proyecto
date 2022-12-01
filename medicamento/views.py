import datetime
from django.shortcuts import render, redirect
from inicio.models import FechaDeDosis
from medicamento.forms import MedicamentoForm
from medicamento.models import Medicamento
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def medicamento(request):
    titulo = 'Medicamentos'
    cargaInicial = Medicamento.objects.all()
    medicamentos = []
  
    fechaContador = datetime.date.today()    

   

    for medicamento in cargaInicial:
        if medicamento.estado != '0':
            medicamentos.append(medicamento)
            fechaContador = medicamento.fechaDosis
            
    

    hoy = datetime.date.today()

    hora = datetime.datetime.now()
    print('arriba', hora)
   
    numero = int(0)
    for medicamento in cargaInicial:
        if fechaContador != hoy:         
            Medicamento.objects.update(contador = numero, fechaDosis = hoy)             
            

    context = {
        'titulo': titulo,
        'medicamentos': medicamentos,
        'url': '',
        'urlCrear': 'crear/',
        'urlListar': 'listar/',
        'fecha': fechaContador
    }
    return render(request, 'medicamentos/medicamentos.html', context)



@login_required
def medicamento_listar(request):
    titulo = 'Medicamentos'
    medicamentos = Medicamento.objects.all()

    for medicamento in medicamentos:
        medicamento.consumoDiario = int(24 / int(medicamento.frecuencia))
        medicamento.alerta = int(4 * medicamento.consumoDiario)
        
    context = {
        'titulo': titulo,
        'medicamentos': medicamentos,
        'url': '../',
        'urlCrear': '../crear/',
        'urlListar': '',
    }
    return render(request, 'medicamentos/medicamentos-listar.html', context)



@login_required
def medicamento_crear(request):
    titulo = 'Medicamentos'
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento creado correctamente')
            return redirect('medicamentos')
        else:
            print('Error')
    else: 
        form = MedicamentoForm()
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../',
        'urlCrear': '',
        'urlListar': '../listar/'
    }
    return render(request, 'medicamentos/medicamentos-crear.html', context)



@login_required
def medicamento_editar(request, pk):
    titulo = 'Medicamentos'
    medicamento = Medicamento.objects.get(id = pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance = medicamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medicamento editado correctamente')
            return redirect('medicamentos')
        else: 
            print('Error al guardar')
    else: 
        form = MedicamentoForm(instance = medicamento)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '',
        'urlListar': '../../listar/'
    }
    return render(request, 'medicamentos/medicamentos-crear.html', context)



@login_required
def medicamento_eliminar(request, pk):
    titulo = 'Eliminar'
    Medicamento.objects.filter(id = pk).update(
        estado = '0'
    )
    return redirect('medicamentos')



@login_required
def medicamento_sumar(request, pk):
    titulo = 'Medicamentos'
    medicamento = Medicamento.objects.get(id = pk)
    #medicamento = Medicamento.objects.filter(id = pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance = medicamento)

        cantidad = int(request.POST.get('cantidad'))
      
    
        nuevo = medicamento.stock
        new = cantidad + nuevo
    
        Medicamento.objects.filter(id = pk).update(
            stock = new
        )
        messages.success(request, 'La cantidad de sumó correctamente')
        return redirect('medicamentos')
    else: 
        form = MedicamentoForm(instance = medicamento)
    context = {
        'titulo': titulo,
        'form': form,
        'url': '../../',
        'urlCrear': '../',
        'urlListar': '../../listar/'
    }
    return render(request, 'medicamentos/medicamentos-sumar.html', context)



@login_required
def medicamento_restar(request, pk):
    titulo = 'Medicamentos'
    medicamento = Medicamento.objects.get(id = pk)
  
    conteo = int(1 + medicamento.contador)
    hora = datetime.datetime.now()

    nuevoStock = int(medicamento.stock - medicamento.dosis)

    Medicamento.objects.filter(id = pk).update(        
        stock = nuevoStock,
        contador = conteo,
        ultimaDosis = hora
    )
    

    return redirect('medicamentos-listar')

    
    
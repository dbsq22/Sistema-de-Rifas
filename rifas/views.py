from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona, NumeroDisponible
from django.contrib import messages
import random

# Create your views here.
def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        numero = request.POST.get('numero')
        if NumeroDisponible.objects.filter(numero=numero).exists():
            NumeroDisponible.objects.filter(numero=numero).delete()
            if form.is_valid():
                form.save()
                messages.success(request, 'Persona agregada exitosamente')
                return redirect('../agregar_personas')
        else:
            messages.error(request, 'Numero repetido')
            return redirect('../agregar_personas')
    else:
        form = PersonaForm()
    numeros_disponibles = NumeroDisponible.objects.all()
    return render(request, 'rifas/agregar_personas.html', {'form': form, 'numeros_disponibles': numeros_disponibles})

def lista_personas(request):
    personas = Persona.objects.order_by('nombre', 'apellido')
    return render(request, 'rifas/lista_personas.html', {'personas': personas})

def index(request):
    return render(request, 'index.html')

def limpiar_listas(request):
    Persona.objects.all().delete()
    NumeroDisponible.objects.all().delete()
    for numero in range(1, 100):
        NumeroDisponible.objects.create(numero=numero)
    return redirect('../lista_personas')

def sortear_ganador(request):
    personas = Persona.objects.all()
    if personas:
        ganador = random.choice(personas)
        messages.success(request, f'El numero ganador es el {ganador.numero}, Felicidades {ganador.nombre} {ganador.apellido}')
    else:
        messages.error(request, 'No hay personas registradas para sortear')
    return redirect('../lista_personas')

def marcar_pago(request):
    if request.method == 'POST':
        for persona in Persona.objects.order_by('nombre', 'apellido'):
            campo_pagado = f'pagado_{persona.id}'
            if campo_pagado in request.POST:
                persona.pagado = True
            else:
                persona.pagado = False
            persona.save()
        mensajes = messages.get_messages(request)
        personas = Persona.objects.all()
        return render(request, 'rifas/lista_personas.html', {'personas': personas, 'messages': mensajes})
    else:
        return redirect('otra_vista')
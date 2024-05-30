from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonaForm
from .models import Persona, NumeroDisponible
from django.contrib import messages
import random

def agregar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            numero = persona.numero
            if NumeroDisponible.objects.filter(numero=numero).exists():
                NumeroDisponible.objects.filter(numero=numero).delete()
                persona.save()
                messages.success(request, 'Persona agregada exitosamente')
            else:
                messages.error(request, 'Número no valido')
            return redirect('rifas:agregar_personas')
        else:
            messages.error(request, 'Numero repetido')
    else:
        form = PersonaForm()
    
    numeros_disponibles = NumeroDisponible.objects.all().order_by('numero')
    return render(request, 'rifas/agregar_personas.html', {'form': form, 'numeros_disponibles': numeros_disponibles})

def lista_personas(request):
    if request.method == 'POST':
        if 'eliminar_persona' in request.POST:
            persona_id = request.POST.get('eliminar_persona')
            if persona_id:
                persona = get_object_or_404(Persona, id=persona_id)
                numero_disponible = NumeroDisponible(numero=persona.numero)
                numero_disponible.save()
                persona.delete()
                messages.success(request, 'Persona eliminada correctamente')
                return redirect('rifas:lista_personas')

            else:
                messages.error(request, 'No se proporcionó un ID válido para eliminar la persona.')

        elif 'guardar_pagos' in request.POST:
            for persona in Persona.objects.all():
                campo_pagado = f'pagado_{persona.id}'
                if campo_pagado in request.POST:
                    persona.pagado = True
                else:
                    persona.pagado = False
                persona.save()
            messages.success(request, 'Cambios guardados correctamente')
            return redirect('rifas:lista_personas')

    personas = Persona.objects.order_by('nombre', 'apellido')
    numeros_disponibles = NumeroDisponible.objects.all().order_by('numero')
    return render(request, 'rifas/lista_personas.html', {'personas': personas, 'numeros_disponibles': numeros_disponibles})

def limpiar_listas(request):
    Persona.objects.all().delete()
    NumeroDisponible.objects.all().delete()
    for numero in range(1, 100):
        NumeroDisponible.objects.create(numero=numero)
    return redirect('rifas:lista_personas')

def sortear_ganador(request):
    personas = Persona.objects.all()
    if personas:
        ganador = random.choice(personas)
        messages.success(request, f'El número ganador es el {ganador.numero}, Felicidades {ganador.nombre} {ganador.apellido}')
    else:
        messages.error(request, 'No hay personas registradas para sortear')
    return redirect('rifas:lista_personas')

def marcar_pago(request):
    if request.method == 'POST':
        for persona in Persona.objects.all():
            campo_pagado = f'pagado_{persona.id}'
            if campo_pagado in request.POST:
                persona.pagado = True
            else:
                persona.pagado = False
            persona.save()
        messages.success(request, 'Cambios guardados correctamente')
    return redirect('rifas:lista_personas')

def index(request):
    return render(request, 'index.html')
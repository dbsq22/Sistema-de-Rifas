from django.urls import path
from .views import agregar_persona, lista_personas, index, limpiar_listas, sortear_ganador, marcar_pago

app_name = 'rifas'

urlpatterns = [
    path('', index, name='index'),
    path('agregar_personas/', agregar_persona, name='agregar_personas'),
    path('lista_personas/', lista_personas, name='lista_personas'),
    path('limpiar_lista/', limpiar_listas, name='limpiar_lista'),
    path('sortear_ganador/', sortear_ganador, name='sortear_ganador'),
    path('marcar_pago/', marcar_pago, name='marcar_pago'),
]
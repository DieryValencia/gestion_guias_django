from django.urls import path
from . import views

urlpatterns = [
    path('profesor/crear/', views.crear_guia, name='crear_guia'),
    path('monitor/listar/', views.listar_guias, name='listar_guias'),
    path('monitor/asignar/', views.asignar_recursos, name='asignar_recursos'),
    path('estudiante/consultar/', views.consultar_guias, name='consultar_guias'),
]

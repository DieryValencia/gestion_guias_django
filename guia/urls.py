
from django.urls import path
from . import views


app_name = 'guia'

urlpatterns = [
    path('',           views.GuiaListView.as_view(),   name='guia_list'),
    path('nueva/',     views.GuiaCreateView.as_view(), name='guia_create'),
    path('editar/<int:pk>/', views.GuiaUpdateView.as_view(), name='guia_update'),
    path('eliminar/<int:pk>/', views.GuiaDeleteView.as_view(), name='guia_delete'),
]

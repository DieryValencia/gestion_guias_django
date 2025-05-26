from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

def home(request):
    return redirect('guia:guia_create')

urlpatterns = [
    path('',                 home, name='home'),
    path('guia/',            include('guia.urls', namespace='guia')),
    path('accounts/',        include('django.contrib.auth.urls')),  # <--- ojo aquí
    path('admin/',           admin.site.urls),
]

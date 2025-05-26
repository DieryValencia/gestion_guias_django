#from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

def home(request):
    return redirect('crear_guia')

urlpatterns = [
    path('', home, name='home'),
    path('crear_guia/', include('guia.urls')),
   #path('admin/', admin.site.urls),
]

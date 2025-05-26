from django.shortcuts import render, redirect
guias = []

def crear_guia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        tema = request.POST.get('tema')
        if titulo and tema:
            guia = {'id': len(guias) + 1, 'title': titulo, 'tema': tema, 'resources': ''}
            guias.append(guia)
            return redirect('listar_guias')
    return render(request, 'crear_guia.html')

def listar_guias(request):
    if request.method == 'POST':
        gid = int(request.POST.get('id'))
        recurso = request.POST.get('resources')
        for guia in guias:
            if guia['id'] == gid:
                guia['resources'] = recurso
                break
    return render(request, 'revisar_guias.html', {'guias': guias})

def consultar_guias(request):
    return render(request, 'consultar_guias.html', {'guias': guias})

def asignar_recursos(request):
    return redirect('listar_guias')

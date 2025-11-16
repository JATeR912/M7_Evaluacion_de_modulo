from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Etiqueta
from .forms import EtiquetaForm

# LISTA
@login_required
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas_app/lista.html', {'etiquetas': etiquetas})

# CREAR
@login_required
def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    return render(request, 'etiquetas_app/formulario.html', {'form': form, 'titulo': 'Crear Etiqueta'})

# EDITAR
@login_required
def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    return render(request, 'etiquetas_app/formulario.html', {'form': form, 'titulo': 'Editar Etiqueta'})

# ELIMINAR
@login_required
def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    if request.method == 'POST':
        etiqueta.delete()
        return redirect('lista_etiquetas')
    return render(request, 'etiquetas_app/eliminar.html', {'etiqueta': etiqueta})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Categoria
from .forms import CategoriaForm

# LISTA
@login_required
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias_app/lista.html', {'categorias': categorias})

# CREAR
@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias_app/formulario.html', {'form': form, 'titulo': 'Crear Categoría'})

# EDITAR
@login_required
def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias_app/formulario.html', {'form': form, 'titulo': 'Editar Categoría'})

# ELIMINAR
@login_required
def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'categorias_app/eliminar.html', {'categoria': categoria})

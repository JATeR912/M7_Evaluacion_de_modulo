from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, DetalleProducto
from .forms import ProductoForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# VISTA PRINCIPAL
def index(request):
    return render(request, 'index.html')

# LISTA
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos_app/lista.html', {'productos': productos})

# DETALLE
@login_required
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos_app/detalle.html', {'producto': producto})

# CREAR
@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()

            # Crear detalles del producto
            DetalleProducto.objects.create(
                producto=producto,
                dimension=form.cleaned_data['dimension'],
                peso=form.cleaned_data['peso']
            )

            form.save_m2m()  
            return redirect('detalle_producto', id=producto.id)
    else:
        form = ProductoForm()
    return render(request, 'productos_app/crear.html', {'form': form})

# EDITAR
@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    try:
        detalle = producto.detalle 
    except DetalleProducto.DoesNotExist:
        detalle = None

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()

            if detalle:
                detalle.dimension = form.cleaned_data['dimension']
                detalle.peso = form.cleaned_data['peso']
                detalle.save()
            else:
                DetalleProducto.objects.create(
                    producto=producto,
                    dimension=form.cleaned_data['dimension'],
                    peso=form.cleaned_data['peso']
                )

            form.save_m2m()
            return redirect('detalle_producto', id=producto.id)
    else:
        initial = {}
        if detalle:
            initial = {'dimension': detalle.dimension, 'peso': detalle.peso}
        form = ProductoForm(instance=producto, initial=initial)

    return render(request, 'productos_app/editar.html', {
        'form': form,
        'producto': producto
    })

# ELIMINAR
@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == "POST":
        producto.delete()
        messages.success(request, f'Producto "{producto.nombre}" eliminado.')
        return redirect('lista_productos')
    
    return render(request, 'productos_app/eliminar.html', {'producto': producto})

# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_productos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


# LOGOUT
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# REGISTER
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('register')

        # Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registro exitoso. Inicia sesión.')
        return redirect('login')

    return render(request, 'register.html')
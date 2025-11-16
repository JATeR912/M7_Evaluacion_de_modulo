from django.urls import path
from . import views

urlpatterns = [
    # Productos
    path('', views.lista_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('<int:id>/editar/', views.editar_producto, name='editar_producto'),
    path('<int:id>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]
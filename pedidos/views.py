from rest_framework import viewsets
from .models import Restaurante, Producto, Orden, DetalleOrden
from .serializers import RestauranteSerializer, ProductoSerializer, OrdenSerializer, DetalleOrdenSerializer
from rest_framework.permissions import IsAuthenticated

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
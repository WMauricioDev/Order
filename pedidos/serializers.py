from rest_framework import serializers
from .models import Restaurante, Producto, Orden

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    details = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Orden
        fields = '__all__'



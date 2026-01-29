from rest_framework import serializers
from .models import Product, Categorie, Place, Compare, DailySale, Debt, UnitPricing

# 1. Serializador para los precios detallados
class UnitPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitPricing
        fields = ['individual_sale_price', 'bulk_quantity', 'bulk_price']

# 2. Serializador de Productos (con lógica para crear/actualizar precios detalle)
class ProductSerializer(serializers.ModelSerializer):
    # Trae el nombre de la categoría para lectura fácil
    name_category = serializers.CharField(source='category.name', read_only=True)
    
    # Anidamos el detalle de precios
    unit_pricing = UnitPricingSerializer(required=False)

    class Meta:
        model = Product
        fields = '__all__' # Corregido: llevaba dos guiones bajos al final

    def create(self, validated_data):
        # Extraemos los datos de precios detallados antes de crear el producto
        unit_pricing_data = validated_data.pop('unit_pricing', None)
        product = Product.objects.create(**validated_data)
        
        if unit_pricing_data:
            UnitPricing.objects.create(product=product, **unit_pricing_data)
        return product

    def update(self, instance, validated_data):
        # Extraemos los datos de precios para la actualización
        unit_pricing_data = validated_data.pop('unit_pricing', None)
        
        # Actualizamos los campos básicos del producto
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Si vienen datos de precios, los actualizamos o los creamos si no existían
        if unit_pricing_data:
            UnitPricing.objects.update_or_create(
                product=instance, 
                defaults=unit_pricing_data
            )
        return instance

# --- Resto de Serializers ---

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__' # Cambiado a all para que incluya todo lo que definas
        

class CompareSerializer(serializers.ModelSerializer):
    # Esto permite que la App muestre los nombres directamente sin hacer otra petición
    category_name = serializers.CharField(source='category.name', read_only=True)
    place_name = serializers.CharField(source='place.name', read_only=True)

    class Meta:
        model = Compare
        fields = '__all__'

class DailySaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySale
        fields = '__all__' 

class DebtSerializer(serializers.ModelSerializer):
    # Si la deuda está relacionada con un cliente o usuario, 
    # podrías añadir un campo descriptivo aquí.
    class Meta:
        model = Debt
        fields = '__all__'
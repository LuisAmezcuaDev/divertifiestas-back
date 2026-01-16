from rest_framework import serializers
from .models import Product, Categorie, Place, Compare, DailySale, Debt

class ProductSerializer(serializers.ModelSerializer):
    # Esto traerá el nombre de la categoría en lugar de solo el ID
    name_category = serializers.CharField(source='categorie.name', read_only=True)
    class Meta:
        model = Product
        fields = '__all_'
    # Esto asegura que la URL de la imagen sea absoluta y use HTTPS
    def get_imagen(self, obj):
        if obj.image:
            return obj.image.url
        return None

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name', 'address']

class CompareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compare
        fields = ['id', 'name_product', 'category', 
                  'place', 'look_price', 'register_date'
        ]
class DailySaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySale
        fields = ['id', 'date', 'total_sales', 'observations']  
    

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ['id', 'creditor_name']
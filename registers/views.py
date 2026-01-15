from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Categorie, Place, Compare, DailySale, Debt
from .serializers import ProductSerializer, CategorieSerializer, PlaceSerializer, CompareSerializer, DailySaleSerializer, DebtSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):   
    queryset = Product.objects.all()  
    serializer_class = ProductSerializer

class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer 

class compareViewSet(viewsets.ModelViewSet):
    queryset = Compare.objects.all()
    serializer_class = CompareSerializer

class DailySaleViewSet(viewsets.ModelViewSet):
    queryset = DailySale.objects.all()
    serializer_class = DailySaleSerializer

class DebtViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
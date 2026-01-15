from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategorieViewSet, PlaceViewSet, compareViewSet, DailySaleViewSet, DebtViewSet

# Crear el router y registrar nuestro viewsets
router = DefaultRouter()
router.register(r'products', ProductViewSet),
router.register(r'categories', CategorieViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'compares', compareViewSet)
router.register(r'dailysales', DailySaleViewSet)
router.register(r'debts', DebtViewSet)
# La API URLs están ahora determinadas automáticamente por el router
urlpatterns = [
    path('', include(router.urls)),

]
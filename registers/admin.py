from django.contrib import admin
from .models import Categorie, Place, Product, Compare, DailySale, Debt

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Place)
admin.site.register(Product)
admin.site.register(Compare)
admin.site.register(DailySale)  
admin.site.register(Debt)
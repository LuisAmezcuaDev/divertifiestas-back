from django.contrib import admin
from .models import Categorie, Place, Product, Compare, DailySale, Debt, UnitPricing

# 1. Configuramos el Inline
class UnitPricingInline(admin.StackedInline):
    model = UnitPricing
    extra = 1
    max_num = 1
    verbose_name = "Precio al Detalle (Unidad / Granel)"

# 2. Registro de Product con el Inline
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'sale_price', 'units') 
    inlines = [UnitPricingInline] 

# 3. Registro de los demás modelos (Sin repetir Product)
admin.site.register(Categorie)
admin.site.register(Place)
admin.site.register(Compare)
admin.site.register(DailySale)  
admin.site.register(Debt)
# Opcional: Si quieres registrar UnitPricing solo, podrías, 
# pero es mejor dejarlo dentro de Product para evitar desorden.
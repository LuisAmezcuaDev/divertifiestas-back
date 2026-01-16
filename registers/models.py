from django.db import models

# Create your models here.

# Base
class Categorie(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

# Real inventory

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    units = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
    
class Compare(models.Model):
    name_product = models.CharField(max_length=200)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    look_price = models.DecimalField(max_digits=10, decimal_places=2)
    register_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Comparativa de Precio"
        # Ordenar para ver siempre el más barato primero al consultar
        ordering = ['look_price']

    def __str__(self):
        return f"{self.name_product} en {self.place.name}: ${self.look_price}"

    
class DailySale(models.Model):
   date = models.DateField(auto_now_add=True)
   total_sales = models.DecimalField(max_digits=12, decimal_places=2)
   observations = models.TextField(blank=True, null=True)

   def __str__(self):
       return f"Venta {self.date}: ${self.total_sales}"

class Debt(models.Model):
    creditor_name = models.CharField(max_length=200)
    amount_owed = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    is_it_paid = models.BooleanField(default=False)

    def __str__(self):
        estado = "PAGADO" if self.esta_pagada else "PENDIENTE"
        return f"{self.nombre_cliente} - ${self.cantidad_adeudada} ({estado})"
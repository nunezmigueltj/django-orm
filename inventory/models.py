from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos"
    )

    def __str__(self):
        return f"{self.nombre}-{self.precio}"

'''
#1 Get all products.
Producto.objects.all()

#2 Get products that have price > 500
Producto.objects.filter(precio__gt=500) 

#3 Get products without stock
Producto.objects.filter(stock__lt=1) Producto.objects.filter(stock=0)

#4 Get products that the name contains "Pokemon" ignoring uppercase
Producto.objects.filter(nombre__icontains="Pokemon")

#5 Order products based on price
Producto.objects.all().order_by("-precio")

#6 Exclude products of category #3
Producto.objects.exclude(categoria=3)

#7 Get products with category = Cartas
Categoria.objects.get(nombre="Cartas").productos.all()

# 8
Producto.objects.filter(stock=0).exists()


productos = Producto.objects.select_related("categoria").all()

for producto in productos:
    print(producto.nombre)
    print(producto.categoria.nombre)
    print(producto.precio)
'''
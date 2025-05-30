from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class DescuentoPorVolumen(models.Model):
    cantidad_minima = models.IntegerField(null=True, blank=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE)

    def __str__(self):
        return f"Descuento de {self.descuento}% por {self.cantidad_minima} unidades"

class DescuentoTemporal(models.Model):
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Descuento temporal de {self.descuento}%"

class DetallePedido(models.Model):
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    plato = models.ForeignKey('Menu', on_delete=models.CASCADE)
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)

    def __str__(self):
        return f"Detalle de pedido {self.pedido.id} - {self.cantidad} x {self.precio_unitario}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    rol = models.CharField(max_length=50, null=True, blank=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entrada(models.Model):
    fecha = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)

    def __str__(self):
        return f"Entrada de {self.fecha}"

class Factura(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha = models.DateTimeField()
    salida = models.ForeignKey('Salida', on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura {self.id} - Total: {self.total}"

class Menu(models.Model):
    nombre_plato = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, null=True, blank=True)
    disponibilidad = models.BooleanField()

    def __str__(self):
        return self.nombre_plato

class Pedido(models.Model):
    fecha_pedido = models.DateField()
    hora_pedido = models.TimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    unidad_medida = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Promocion(models.Model):
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return f"Promoción de {self.descuento}% en {self.categoria.nombre}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    num_personas = models.IntegerField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva para {self.num_personas} personas"

class Salida(models.Model):
    fecha = models.DateTimeField(null=True, blank=True)
    destino = models.CharField(max_length=100, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Salida {self.id} - Destino: {self.destino}"

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=225)
    rol = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nombre_usuario

from django.db import models

class Fuente(models.Model):
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nombre} ({self.tipo})'


class Cita(models.Model):
    texto = models.TextField()
    autor = models.CharField(max_length=255)
    fecha = models.DateField(null=True, blank=True)
    fuente = models.ForeignKey(Fuente, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'"{self.texto}" - {self.autor}'
from django.db import models

# --- MODELO ETIQUETA ---
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    descripcion = models.TextField(verbose_name='Descripcion')
    image = models.ImageField(verbose_name='Imagen', upload_to="proyects")
    link = models.URLField(null = True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion') # Se crea la primera ves
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion') # Se ejecuta cada ves que se actualiza algo

    class Meta: #metadatos para que aparescan en español
        verbose_name = "projecto"
        verbose_name_plural = "proyectos"
        ordering = ["created"]

    def __str__(self): #para ver el nombre del proyecto en el admin
        return self.title
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = RichTextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Acerca de'
        ordering = ['-created']

    def __str__(self):
        return self.title
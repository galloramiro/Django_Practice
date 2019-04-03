from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Advisors(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    phone = models.CharField(max_length=20, verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Mails', blank=True, null=True)
        
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Asesor Comercial'
        verbose_name_plural = 'Asesores Comerciales'
        ordering = ['created']

    def __str__(self):
        return self.name



class SmgQuotesTable(models.Model):
    composite = models.CharField(max_length=200, verbose_name='Composición')
    smg01 = models.FloatField(verbose_name='SMG01')
    smg02 = models.FloatField(verbose_name='SMG02')
    smg10 = models.FloatField(verbose_name='SMG10')
    smg20 = models.FloatField(verbose_name='SMG20')
    smg30 = models.FloatField(verbose_name='SMG30')
    smg40 = models.FloatField(verbose_name='SMG40')
    smg50 = models.FloatField(verbose_name='SMG50')
    smg60 = models.FloatField(verbose_name='SMG60')
    smg70 = models.FloatField(verbose_name='SMG70')
    
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Valor'
        verbose_name_plural = 'Valores'
        ordering = ['created']

    def __str__(self):
        return self.composite

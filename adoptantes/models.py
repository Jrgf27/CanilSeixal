from django.db import models

# Create your models here.

class Adoptante(models.Model):

    name = models.CharField(max_length=20, null=True)
    idade = models.IntegerField(null=True, blank=True)
    nif = models.IntegerField(null=True, blank=True)
    
    cc = models.IntegerField(null=True, blank=True)
    cc_expiraçao=models.DateField(null=True, blank=True)
    
    
    rua = models.TextField(null=True, default= "", blank=True)
    localidade = models.TextField(null=True, default= "", blank=True)
    cidade = models.TextField(null=True, default= "", blank=True)
    codigo_postal = models.TextField(null=True, default= "", blank=True)
    
    telemovel = models.CharField(max_length=20,null=True, blank=True)
    telefone = models.CharField(max_length=20,null=True, blank=True)
    
    email = models.EmailField(null=True, blank=True)
    profissao = models.TextField(null=True, default= "", blank=True)
    
    has_animal = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.nif}" 

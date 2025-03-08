from django.db import models
from adoptantes.models import Adoptante
# Create your models here.

class Animal(models.Model):
    
    CAO = "cao"
    GATO = "gato"

    ANIMAL_CHOICES = [
        (CAO, "Cão"),
        (GATO, "Gato"),
    ]

    name = models.CharField(max_length=20)
    idade = models.IntegerField()
    cor = models.CharField(max_length=20)
    pelo = models.CharField(max_length=20)
    porte = models.CharField(max_length=20)
    raca = models.CharField(max_length=20)

    descricao = models.TextField(default="")
    informacao_extra = models.TextField(default="")
    comportamento_pessoas = models.TextField(default="")
    comportamento_animais = models.TextField(default="")

    tipo = models.CharField(
        max_length=4,
        choices=ANIMAL_CHOICES,
        default=CAO
    )

    adoptante = models.ForeignKey(Adoptante, on_delete=models.SET_NULL, null=True, blank=True)
    last_update_date = models.DateField(auto_now_add=True)
    adopted_date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.raca}" 



class AnimalImages(models.Model):

    animal=models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, related_name="fotos")
    imagem = models.ImageField(upload_to='%Y/%m/%d')


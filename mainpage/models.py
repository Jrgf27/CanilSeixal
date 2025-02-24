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



class AnimalImages(models.Model):

    animal=models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, related_name="fotos")
    imagem = models.ImageField(upload_to='media/%Y/%m/%d')


from django.db import models

# Create your models here.

class Adoptante(models.Model):

    name = models.CharField(max_length=20, null=True)
    idade = models.IntegerField(null=True, blank=True)
    nif = models.IntegerField(null=True, blank=True)
    mobile = models.CharField(max_length=20)
    cc = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    morada = models.TextField(null=True, default= "", blank=True)
    
    has_animal = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.nif}" 

class Animal(models.Model):
    
    name = models.CharField(max_length=20)
    idade = models.IntegerField()
    cor = models.CharField(max_length=20)
    pelo = models.CharField(max_length=20)
    porte = models.CharField(max_length=20)
    raca = models.CharField(max_length=20)
    
    descricao = models.TextField(default= "")
    
    informacao_extra = models.TextField(default= "")
    
    comportamento_pessoas = models.TextField(default= "")
    comportamento_animais = models.TextField(default= "")
    
    cao = models.BooleanField(default=False)
    gato = models.BooleanField(default=False)

    adoptante=models.ForeignKey(Adoptante, on_delete=models.SET_NULL, null=True, blank=True)
    
    last_update_date = models.DateField(auto_now_add=True)
    adopted_date = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.raca} - {self.last_update_date}" 



class AnimalImages(models.Model):

    animal=models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, related_name="fotos")
    imagem = models.ImageField(upload_to='media/%Y/%m/%d')


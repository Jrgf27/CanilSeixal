from django import forms
from .models import Animal, AnimalImages

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'  # Use all fields from the model
        
        
class AnimalFotosForm(forms.ModelForm):
    class Meta:
        model = AnimalImages
        fields = ('imagem',)  # Use all fields from the model
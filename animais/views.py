from django.shortcuts import HttpResponse, redirect, render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Animal, AnimalImages
from .forms import AnimalForm, AnimalFotosForm

import logging
logger = logging.getLogger("general_logger")


class AnimalList(LoginRequiredMixin, TemplateView):
    def get(self, response):
        
        caes = Animal.objects.filter(tipo="cao")
        gatos = Animal.objects.filter(tipo="gato")
        
        animal_form = AnimalForm()
        
        context = {
            'caes' : caes,
            'gatos' : gatos,
            'animal_form': animal_form,
        }
        
        return render(response, 'animais/animais.html', context)

class AnimalDetails(LoginRequiredMixin, TemplateView):
    def get(self, response, animal_id):
        
        animal = get_object_or_404(Animal, id= animal_id)
        
        form = AnimalFotosForm()
        
        context = {
            'animal' : animal,
            'form' : form
        }
        
        return render(response, 'animais/partials/animal_modal.html', context)
    
    def post(self, response):
        
        form = AnimalForm(response.POST)
        if form.is_valid():
            animal = form.save()
            context = {
                'animal' : animal
            }
            return render(response, 'animais/partials/animal_avatar.html', context)
        
        logger.info(form.errors)
        return HttpResponse("Falha a salvar!")

class AnimalImagens(LoginRequiredMixin, TemplateView):
    def post(self, response, animal_id):
        
        form = AnimalFotosForm(response.POST, response.FILES)
        
        if form.is_valid():
            animal = get_object_or_404(Animal, id= animal_id)
            
            AnimalImages.objects.create(
                animal = animal,
                imagem = form.cleaned_data['imagem']
            )
            form = AnimalFotosForm()
            
            context = {
                'form': form,
                'animal' : animal
            }
            return render(response, 'animais/partials/animal_modal_fotos.html', context)

        
        logger.info(form.errors)
        return HttpResponse("Falha a salvar!")


from django.shortcuts import HttpResponse, redirect, render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Animal, AnimalImages, Adoptante
from .forms import AnimalForm, AnimalFotosForm, AdoptanteForm

import logging
logger = logging.getLogger("general_logger")


class Homepage(LoginRequiredMixin, TemplateView):
    def get(self, response):
        
        caes = Animal.objects.filter(tipo="cao")
        gatos = Animal.objects.filter(tipo="gato")
        
        animal_form = AnimalForm()
        
        context = {
            'caes' : caes,
            'gatos' : gatos,
            'animal_form': animal_form,
        }
        
        return render(response, 'mainpage/homepage.html', context)

class AnimalDetails(LoginRequiredMixin, TemplateView):
    def get(self, response, animal_id):
        
        animal = get_object_or_404(Animal, id= animal_id)
        
        form = AnimalFotosForm()
        
        context = {
            'animal' : animal,
            'form' : form
        }
        
        return render(response, 'mainpage/partials/animal_details.html', context)
    
    def post(self, response):
        
        form = AnimalForm(response.POST)
        if form.is_valid():
            animal = form.save()
            context = {
                'animal' : animal
            }
            return render(response, 'mainpage/partials/animal_card_details.html', context)
        
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
            return render(response, 'mainpage/partials/animal_fotos_details.html', context)

        
        logger.info(form.errors)
        return HttpResponse("Falha a salvar!")


class Adoptantes(LoginRequiredMixin, TemplateView):
    def get(self, response):
        
        adoptantes = Adoptante.objects.all()
        
        adoptante_form = AdoptanteForm()
        
        context = {
            'adoptantes' : adoptantes,
            'adoptante_form': adoptante_form,
        }
        
        return render(response, 'mainpage/adoptantes.html', context)
    
    def post(self, response):
        
        form = AdoptanteForm(response.POST)
        if form.is_valid():
            adoptante = form.save()
            context = {
                'adoptante' : adoptante
            }
            return render(response, 'mainpage/partials/adoptante_details.html', context)
        
        logger.info(form.errors)
        return HttpResponse("Falha a salvar!")


class AdoptanteDetails(LoginRequiredMixin, TemplateView):
    def get(self, response, adoptante_id):
        
        adoptante = get_object_or_404(Adoptante, id= adoptante_id)
        context = {
            'adoptante' : adoptante,
        }
        
        return render(response, 'mainpage/partials/adoptante_modal.html', context)


class HealthCheck(TemplateView):
    def get(self, response):
        return HttpResponse('OK')
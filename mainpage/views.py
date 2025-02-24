from django.shortcuts import HttpResponse, redirect, render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



from .models import Animal, AnimalImages, Adoptante
from .forms import AnimalForm


class Homepage(LoginRequiredMixin, TemplateView):
    def get(self, response):
        
        caes = Animal.objects.filter(cao=True)
        gatos = Animal.objects.filter(gato=True)
        
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
        
        context = {
            'animal' : animal,
        }
        
        return render(response, 'mainpage/partials/animal_details.html', context)


class HealthCheck(TemplateView):
    def get(self, response):
        return HttpResponse('OK')
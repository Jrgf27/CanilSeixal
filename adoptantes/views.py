from django.shortcuts import HttpResponse, redirect, render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Adoptante
from .forms import AdoptanteForm

import logging
logger = logging.getLogger("general_logger")


class AdoptantesList(LoginRequiredMixin, TemplateView):
    def get(self, response):
        
        adoptantes = Adoptante.objects.all()
        
        adoptante_form = AdoptanteForm()
        
        context = {
            'adoptantes' : adoptantes,
            'adoptante_form': adoptante_form,
        }
        
        return render(response, 'adoptantes/adoptantes.html', context)
    

class AdoptanteDetails(LoginRequiredMixin, TemplateView):
    def get(self, response, adoptante_id):
        
        adoptante = get_object_or_404(Adoptante, id= adoptante_id)
        context = {
            'adoptante' : adoptante,
        }
        
        return render(response, 'adoptantes/partials/adoptante_modal.html', context)
    
    def post(self, response):
        
        form = AdoptanteForm(response.POST)
        if form.is_valid():
            adoptante = form.save()
            context = {
                'adoptante' : adoptante
            }
            return render(response, 'adoptantes/partials/adoptante_row.html', context)
        
        logger.info(form.errors)
        return HttpResponse("Falha a salvar!")

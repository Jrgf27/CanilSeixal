from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.AnimalList.as_view(), name='animais'),

    path('animal/<int:animal_id>', views.AnimalDetails.as_view(), name='get_animal_details'),
    path('animal', views.AnimalDetails.as_view(), name='save_animal_details'),
    
    path('animal-image/<int:animal_id>', views.AnimalImagens.as_view(), name='save_animal_image'),
    
]

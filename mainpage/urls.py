from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Homepage.as_view(), name='animais'),
    path('load-animal-details/<int:animal_id>', views.AnimalDetails.as_view(), name='load_animal_details'),
    path('save-animal-details', views.AnimalDetails.as_view(), name='save_animal_details'),
    
    
    path('save-animal-image/<int:animal_id>', views.AnimalImagens.as_view(), name='save_animal_image'),
    
    
    path('adotantes', views.Homepage.as_view(), name='adotantes'),
    path('health', views.HealthCheck.as_view(), name='health'),
]

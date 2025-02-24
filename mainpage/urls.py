from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Homepage.as_view(), name='animais'),
    path('load-animal-details/<int:animal_id>', views.AnimalDetails.as_view(), name='load_animal_details'),
    
    
    path('adotantes', views.Homepage.as_view(), name='adotantes'),
    path('health', views.HealthCheck.as_view(), name='health'),
]

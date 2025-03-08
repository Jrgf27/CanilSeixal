from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.AdoptantesList.as_view(), name='adotantes'),
    path('adoptante/<int:adoptante_id>', views.AdoptanteDetails.as_view(), name='get_adoptante_details'),
    path('adoptante', views.AdoptanteDetails.as_view(), name='save_adoptante_details'),
    
]

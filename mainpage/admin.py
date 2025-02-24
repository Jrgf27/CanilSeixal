from django.contrib import admin

from .models import Adoptante, Animal, AnimalImages

# Register your models here.

admin.site.register(Adoptante)
admin.site.register(AnimalImages)
admin.site.register(Animal)


from django.contrib import admin

from .models import Animal, AnimalImages

# Register your models here.

admin.site.register(AnimalImages)
admin.site.register(Animal)


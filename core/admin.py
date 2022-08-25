from django.contrib import admin

# Register your models here.

from core.models import Carro, Categoria, Marca

admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Carro)

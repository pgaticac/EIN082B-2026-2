from django.contrib import admin
from .models import Carrera

class CarreraAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','duracion']
    ordering = ['duracion']


admin.site.register(Carrera,CarreraAdmin)

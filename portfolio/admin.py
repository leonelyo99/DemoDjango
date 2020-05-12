from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin): #para que muestre campos ocultos
    readonly_fields = ('created', 'update')


# Register your models here.
admin.site.register(Project, ProjectAdmin)
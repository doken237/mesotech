from django.contrib import admin

# Register your models here.
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    
    list_display = ["prenom","nom","email","tel","message","created","updated"]

admin.site.register(Client,ClientAdmin)

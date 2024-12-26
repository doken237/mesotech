from django.contrib import admin
from .models import Cathegory, Produit

# Register your models here.

class CathegoryAdmin(admin.ModelAdmin):
    
    list_display = ["libelle","created","updated"]
    

class ProduitAdmin(admin.ModelAdmin):
  
    list_display = ["designation","pv","etat","id_category","photo","caracteristique","created","updated"]
    readonly_fields = ('image_height', 'image_width', "created", "updated")



admin.site.register(Cathegory,CathegoryAdmin)
admin.site.register(Produit,ProduitAdmin)
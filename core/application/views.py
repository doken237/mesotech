from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from core.produit.models import Produit


# Create your views here.

def application_view(request):
     return render(request, 'application/base.html')



def afficher_produits(request):
    produits = Produit.objects.all()  # Filtrer les produits si nécessaire
    print(produits)


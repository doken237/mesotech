from django.http import HttpResponseRedirect
from django.shortcuts import render
from produit.forms import ProduitRegistration
from .models import Produit

def add_show(request):
    if request.method == 'POST':
        fm = ProduitRegistration(request.POST, request.FILES)
        
        if fm.is_valid():
            # Sauvegarde du formulaire si les données sont valides
            fm.save()
            fm = ProduitRegistration()  # Réinitialiser le formulaire après enregistrement
        else:
            print(fm.errors)  # Afficher les erreurs dans la console

    else:
        fm = ProduitRegistration()

    # Récupérer tous les produits pour les afficher
    produits = Produit.objects.all()

    return render(request, 'produit/addandshow.html', {'form': fm, 'produits': produits})

# cete fonction permet de mofifier les informations
def update_data(request,id):
    if request.method=="POST":
        pi=Produit.objects.get(pk=id)
        fm=ProduitRegistration(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Produit.objects.get(pk=id)
        fm=ProduitRegistration(instance=pi)
    return render(request,'produit/updatestudient.html',{'form':fm})


#cette fonction permet de supprimer les donnees d'un etudiant

def delete_data(request,id):
    if request.method=="POST":
        pi=Produit.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    


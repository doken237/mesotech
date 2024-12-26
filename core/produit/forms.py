from django import forms
from .models import Produit, Cathegory

class ProduitRegistration(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ["designation", "pv", "etat", "id_category", "photo", "caracteristique"]

        # Widgets doivent être correctement définis
        widgets = {
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'pv': forms.NumberInput(attrs={'class': 'form-control'}),
            'etat': forms.Select(attrs={'class': 'form-control'}),  # Widget correct
            'id_category': forms.Select(attrs={'class': 'form-control'}),  # Widget correct
            'caracteristique': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    # La méthode __init__ doit être définie au bon endroit
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Récupérer les choix pour id_category depuis la base de données
        self.fields['id_category'].choices = [
            (cat.id, cat.libelle) for cat in Cathegory.objects.all()
        ]

    # Ajouter les choix pour le champ "etat" (si ce n'est pas dans le modèle)
    ETAT_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ]
    etat = forms.ChoiceField(choices=ETAT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

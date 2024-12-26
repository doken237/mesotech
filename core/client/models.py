from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Client(models.Model):
    prenom=models.CharField( max_length=150)
    nom=models.CharField( max_length=150)
    email=models.EmailField( max_length=254)
    tel = PhoneNumberField(region="CM")
    message=models.CharField( max_length=2500)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom} - {self.tel}"
# Create your models here.

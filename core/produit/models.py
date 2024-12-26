from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import io


# Create your models here.
class Cathegory(models.Model):
    libelle=models.CharField( max_length=100, unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.libelle)


class Produit(models.Model):
    ETAT_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
    ]
    # image_height = models.PositiveIntegerField(null=True, blank=True, default=0, editable=False)
    # image_width = models.PositiveIntegerField(null=True, blank=True,default=0, editable=False)
    designation=models.CharField( max_length=150)
    pv = models.FloatField(
        default=0.0,
        null=True,
        blank=True,
        validators=[MinValueValidator(500), MaxValueValidator(1000000.0)],
        help_text="Prix de vente du produit, en euros.",
        verbose_name="Prix de Vente",
        unique=False,
        db_index=True
    )
    etat=models.CharField( max_length=150,choices=ETAT_CHOICES,default='pending',verbose_name='État')
    id_category=models.ForeignKey("cathegory", related_name="cathegory", verbose_name=("id_cathegory"),on_delete=models.CASCADE)
    caracteristique=models.CharField( max_length=2000)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    photo=models.ImageField(("IMAGE"), upload_to="photos", height_field="image_height",
        width_field="image_width",max_length=255)
    image_height = models.PositiveIntegerField(editable=False, null=True)
    image_width = models.PositiveIntegerField(editable=False, null=True)

    def save(self, *args, **kwargs):
        # Si l'image a été modifiée ou est nouvelle, redimensionnez-la
        if self.photo:
            img = Image.open(self.photo)

            # Redimensionner l'image (par exemple, largeur de 500px, hauteur auto-calculée)
            max_width = 500
            width_percent = (max_width / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(width_percent)))
            img = img.resize((max_width, h_size), Image.Resampling.LANCZOS)
            

            # Sauvegarder l'image dans un fichier mémoire pour remplacer le fichier original
            img_io = io.BytesIO()
            img.save(img_io, format='JPEG')
            img_io.seek(0)

            # Créer un fichier InMemoryUploadedFile pour le stockage
            self.photo = InMemoryUploadedFile(img_io, None, self.photo.name, 'image/jpeg', img_io.getbuffer().nbytes, None)

        # Appeler la méthode save originale
        super(Produit, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.designation)

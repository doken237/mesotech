"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from produit import views as prod
from application import views as  app 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', prod.add_show, name='home'),
    path('update_data/<int:id>/', prod.update_data, name='updatedata'),
    path('delete/<int:id>/',prod.delete_data,name="deletedata"),
    path('application/', app.application_view, name='application'),
    path('categorie', app.afficher_produits, name='produits_par_categorie'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
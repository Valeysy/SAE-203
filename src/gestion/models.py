from django.db import models
from django.utils import timezone
from datetime import timedelta

class Aeroport(models.Model):
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} ({self.pays})"
        
    class Meta:
        db_table = 'aeroport'

class Piste(models.Model):
    numero = models.IntegerField()
    aeroport = models.ForeignKey(Aeroport, on_delete=models.CASCADE)
    longueur = models.IntegerField()

    def __str__(self):
        return f"Piste {self.numero} - {self.aeroport.nom}"
    
    class Meta:
        db_table = 'piste'

class Compagnie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    pays_attache = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'compagnie'


class TypeAvion(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    description = models.TextField()
    longueur_piste_necessaire = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"{self.marque} {self.modele}"
    
    class Meta:
        db_table = 'typeavion'


class Avion(models.Model):
    nom = models.CharField(max_length=100)
    compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    modele = models.ForeignKey(TypeAvion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
    
    class Meta:
        db_table = 'avion'


class Vol(models.Model):
    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    pilote = models.CharField(max_length=100)
    aeroport_depart = models.ForeignKey(Aeroport, related_name='depart_vols', on_delete=models.CASCADE)
    date_heure_depart = models.DateTimeField()
    aeroport_arrivee = models.ForeignKey(Aeroport, related_name='arrivee_vols', on_delete=models.CASCADE)
    date_heure_arrivee = models.DateTimeField()

    def __str__(self):
        return f"Vol {self.avion.nom} de {self.aeroport_depart.nom} à {self.aeroport_arrivee.nom}"
            
    class Meta:
        db_table = 'vol'

            

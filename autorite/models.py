from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
class Autorite(models.Model):
    nom = models.CharField(name="nom", max_length=50, default="")
    type = models.CharField(name="type", max_length=50, default="")
    telephone = models.CharField(name="telephone", max_length=9, default="")
    addresse = models.CharField(name="addresse", max_length=40, default="")
    zone_couverture = models.CharField(name="zone_couverture", max_length=40, default="")
    personnel = models.IntegerField(name="personnel", default=0)
    vehicules = models.IntegerField(name="vehicules", default=0)
    status = models.CharField(name="status", max_length=40, default="")
    email = models.CharField(name="email", max_length=50, default="")
    password = models.CharField(name="password", max_length=128)

    def save(self, *args, **kwargs):
        # Hasher le mot de passe avant de le sauvegarder
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

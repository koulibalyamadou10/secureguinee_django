from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
class SCUser(models.Model):
    nom = models.CharField(name="nom", max_length=30, default="")
    prenom = models.CharField(name="prenom", max_length=30, default="")
    numero = models.CharField(name="numero", max_length=9)
    password = models.CharField(name="password", max_length=128)

    def save(self, *args, **kwargs):
        # Hasher le mot de passe avant de le sauvegarder
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


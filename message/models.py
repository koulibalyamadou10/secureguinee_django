from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(to="user.SCUser" , on_delete=models.CASCADE, related_name="messages_sent", null=True)  # Expéditeur
    recipient = models.ForeignKey(to="autorite.Autorite", on_delete=models.CASCADE, related_name="messages_received", null=True)  # Destinataire
    message = models.TextField(name="message", null=True)
    sent_at = models.DateTimeField(auto_now_add=True)  # Date d'envoi
    is_read = models.BooleanField(default=False)  # Indique si le message a été lu par l'autorité
    is_sent_by_user = models.BooleanField(default=True)  # Indique si le message a été lu par l'autorité
    image = models.ImageField(upload_to='uploaded_images/', null=True)


# Generated by Django 5.1.3 on 2024-12-01 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autorite', '0001_initial'),
        ('message', '0002_message_is_sent_by_user'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to='uploaded_images/'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages_received', to='autorite.autorite'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages_sent', to='user.scuser'),
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SCUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=30)),
                ('prenom', models.CharField(default='', max_length=30)),
                ('numero', models.CharField(max_length=9)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]

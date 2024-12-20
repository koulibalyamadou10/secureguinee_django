# Generated by Django 5.1.3 on 2024-12-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=50)),
                ('type', models.CharField(default='', max_length=50)),
                ('telephone', models.CharField(default='', max_length=9)),
                ('addresse', models.CharField(default='', max_length=40)),
                ('zone_couverture', models.CharField(default='', max_length=40)),
                ('personnel', models.IntegerField(default=0)),
                ('vehicules', models.IntegerField(default=0)),
                ('status', models.CharField(default='', max_length=40)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]

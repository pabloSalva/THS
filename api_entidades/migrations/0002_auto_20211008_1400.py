# Generated by Django 3.0.8 on 2021-10-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_entidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localidad',
            name='entidad',
            field=models.ManyToManyField(null=True, related_name='entidad', to='api_entidades.Entidad'),
        ),
    ]

# Generated by Django 3.0.8 on 2021-10-08 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ambiente',
            name='cerramiento',
        ),
        migrations.AddField(
            model_name='cerramiento',
            name='ambiente',
            field=models.ManyToManyField(null=True, related_name='cerramiento', to='api_inmuebles.Ambiente'),
        ),
    ]

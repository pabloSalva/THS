# Generated by Django 3.0.8 on 2022-02-16 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_artefactos', '0012_auto_20220216_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artefacto',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='artefacto',
            name='modelo',
        ),
        migrations.AddField(
            model_name='artefacto',
            name='marca_modelo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api_artefactos.Modelo'),
        ),
    ]
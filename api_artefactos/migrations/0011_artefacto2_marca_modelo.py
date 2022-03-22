# Generated by Django 3.0.8 on 2022-02-16 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_inmuebles', '0009_remove_ambiente_clasificacion'),
        ('api_artefactos', '0010_auto_20220216_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_artefactos.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Artefacto2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etiqueta', models.IntegerField(choices=[(0, 'A+++'), (1, 'A++'), (2, 'A+'), (3, 'A'), (4, 'B'), (5, 'C'), (6, 'D'), (7, 'E'), (8, 'F'), (9, 'G')], default=0, max_length=4)),
                ('nombre', models.CharField(max_length=50)),
                ('consumo', models.IntegerField(default=0)),
                ('calor_residual', models.FloatField(default=0.0)),
                ('categoria', models.IntegerField(choices=[(0, 'Aires'), (1, 'heladeras'), (2, 'Electronica'), (3, 'Iluminación'), (5, 'Lavarropas'), (4, 'Cocina'), (6, 'Calefacción'), (7, 'Baño'), (8, 'Agua')], default=0)),
                ('descripcion', models.CharField(max_length=500)),
                ('tipo', models.CharField(choices=[('EL', 'Electrico'), ('GS', 'Gas')], default='EL', max_length=2)),
                ('ambientes', models.ManyToManyField(blank=True, null=True, to='api_inmuebles.Ambiente')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_artefactos.Modelo')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
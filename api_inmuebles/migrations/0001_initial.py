# Generated by Django 3.0.8 on 2021-08-27 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_artefactos', '0002_artefacto_users'),
        ('api_entidades', '0002_entidad_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('conductividad', models.FloatField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('cantidad_personas', models.IntegerField(default=1)),
                ('antiguedad', models.IntegerField()),
                ('estiqueta', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E'), (5, 'F'), (6, 'G')], default=0)),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_entidades.Localidad')),
            ],
        ),
        migrations.CreateModel(
            name='Cerramiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=255)),
                ('superficie', models.FloatField(max_length=15)),
                ('es_externo', models.BooleanField(default=False)),
                ('tipo', models.CharField(choices=[('Ventana', 'ventana'), ('Techo', 'techo'), ('Pared', 'pared'), ('Puerta', 'puerta')], default='Pared', max_length=7)),
                ('orientacion', models.CharField(choices=[('N', 'norte'), ('S', 'sur'), ('E', 'este'), ('O', 'oeste'), ('NO', 'noroeste'), ('SE', 'sureste'), ('NE', 'noreste'), ('SO', 'sureste')], default='N', max_length=8)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_inmuebles.Material')),
            ],
        ),
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=255)),
                ('volumen', models.FloatField(max_length=15)),
                ('clasificacion', models.CharField(max_length=255)),
                ('artefacto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_artefactos.Artefacto')),
                ('cerramiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api_inmuebles.Cerramiento')),
            ],
        ),
    ]

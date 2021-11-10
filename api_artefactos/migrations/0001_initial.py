# Generated by Django 3.0.8 on 2021-09-05 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_inmuebles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artefacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('consumo', models.IntegerField(default=0)),
                ('calor_residual', models.FloatField(default=0.0)),
                ('categoria', models.IntegerField(choices=[(0, 'Aires'), (1, 'Linea blanca'), (2, 'Electronica'), (3, 'Iluminación'), (4, 'Calefacción')], default=0)),
                ('descripcion', models.CharField(max_length=50)),
                ('marca', models.CharField(default='', max_length=20)),
                ('modelo', models.CharField(default='', max_length=20)),
                ('tipo', models.CharField(choices=[('EL', 'Electrico'), ('GS', 'Gas')], default='EL', max_length=2)),
                ('ambientes', models.ManyToManyField(blank=True, null=True, to='api_inmuebles.Ambiente')),
                ('etiqueta', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='api_inmuebles.Etiqueta')),
            ],
        ),
    ]

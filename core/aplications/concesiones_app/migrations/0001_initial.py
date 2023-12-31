# Generated by Django 4.2.2 on 2023-06-22 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concesiones',
            fields=[
                ('numero_concesion', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('tipo_concesion', models.CharField(max_length=50)),
                ('comuna', models.CharField(max_length=30)),
                ('lugar', models.CharField(max_length=30)),
                ('rs_ds', models.CharField(max_length=15)),
                ('tipo_tramite', models.CharField(max_length=50)),
                ('concesionario', models.CharField(max_length=30)),
                ('tipo_vigencia', models.CharField(max_length=50)),
            ],
        ),
    ]

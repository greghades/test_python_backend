# Generated by Django 4.2.2 on 2023-06-22 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesiones_app', '0007_alter_concesiones_comuna_alter_concesiones_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concesiones',
            name='comuna',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='concesiones',
            name='lugar',
            field=models.CharField(max_length=150),
        ),
    ]

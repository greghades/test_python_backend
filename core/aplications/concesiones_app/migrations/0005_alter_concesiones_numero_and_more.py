# Generated by Django 4.2.2 on 2023-06-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesiones_app', '0004_alter_concesiones_tipo_concesion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concesiones',
            name='numero',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='concesiones',
            name='tipo_tramite',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='concesiones',
            name='tipo_vigencia',
            field=models.CharField(max_length=150),
        ),
    ]
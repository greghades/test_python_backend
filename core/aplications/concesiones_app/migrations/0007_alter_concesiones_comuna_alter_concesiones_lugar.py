# Generated by Django 4.2.2 on 2023-06-22 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesiones_app', '0006_alter_concesiones_numero_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concesiones',
            name='comuna',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='concesiones',
            name='lugar',
            field=models.CharField(max_length=50),
        ),
    ]

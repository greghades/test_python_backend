# Generated by Django 4.2.2 on 2023-06-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisprudencias_app', '0004_alter_jurisprudencias_competencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='materia',
            field=models.CharField(max_length=50),
        ),
    ]

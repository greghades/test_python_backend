# Generated by Django 4.2.2 on 2023-06-20 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisprudencias_app', '0002_alter_descriptores_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='caratulado',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jurisprudencias',
            name='url_doc',
            field=models.CharField(max_length=100),
        ),
    ]

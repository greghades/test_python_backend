# Generated by Django 4.2.2 on 2023-06-21 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jurisprudencias_app', '0006_remove_jurisprudencias_url_doc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jurisprudencias',
            name='caratulado',
            field=models.CharField(max_length=200),
        ),
    ]

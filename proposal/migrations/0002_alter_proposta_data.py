# Generated by Django 4.0.1 on 2022-01-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='data',
            field=models.DateField(verbose_name='Data de Emissão'),
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-19 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_agendamento_proprietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='status',
            field=models.CharField(choices=[('A', 'Agendado'), ('F', 'Finalizado'), ('C', 'Cancelado')], default='A', max_length=1),
        ),
    ]
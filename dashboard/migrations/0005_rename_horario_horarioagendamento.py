# Generated by Django 4.0.1 on 2022-01-19 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_agendamento_horarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Horario',
            new_name='HorarioAgendamento',
        ),
    ]

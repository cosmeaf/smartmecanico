# Generated by Django 4.0.1 on 2022-01-19 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_horario_horarioagendamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='dias_visita',
        ),
        migrations.AddField(
            model_name='agendamento',
            name='dias_visita',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.diasvisita'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='horarios',
        ),
        migrations.AddField(
            model_name='agendamento',
            name='horarios',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.horarioagendamento'),
            preserve_default=False,
        ),
    ]

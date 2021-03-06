# Generated by Django 4.0.1 on 2022-01-18 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, max_length=14, verbose_name='CPF')),
                ('cnpj', models.CharField(blank=True, max_length=18, verbose_name='CNPJ')),
                ('endereco', models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço')),
                ('bairro', models.CharField(blank=True, max_length=255, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, null=True, verbose_name='Estato')),
                ('data', models.CharField(max_length=10, verbose_name='Data de Emissão')),
                ('validade', models.CharField(blank=True, choices=[('Quinze', '15 (Quinze)'), ('Trinta', '30 (Trinta)'), ('Sessenta', '60 (Sessenta)'), ('Noventa', '90 (Noventa)')], max_length=255, null=True, verbose_name='Validade')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Valor')),
                ('situacao', models.CharField(blank=True, choices=[('Atrasado', 'Atrasado'), ('AVencer', 'Á Vencer'), ('Pago', 'Pago')], max_length=255, null=True, verbose_name='Situação')),
                ('pago', models.BooleanField(default=False)),
                ('dominio', models.CharField(blank=True, help_text='URL - exe: seudomiio.com.br', max_length=255, null=True, verbose_name='Dominio do Site')),
                ('dominio_login', models.CharField(blank=True, help_text='URL - exe: seudomino.com.br/admin', max_length=255, null=True, verbose_name='Acesso ao Admin')),
                ('login', models.CharField(blank=True, max_length=20, null=True, verbose_name='Login')),
                ('senha', models.CharField(blank=True, max_length=20, null=True, verbose_name='Senha')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proposal.cliente')),
            ],
            options={
                'verbose_name': 'UMA PROPOSTA',
                'verbose_name_plural': 'PROPOSTAS',
                'ordering': ['-data'],
            },
        ),
    ]

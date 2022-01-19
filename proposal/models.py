from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.db.models import Sum, Avg
from localflavor.br.br_states import STATE_CHOICES
from django.utils.safestring import mark_safe
from django.contrib.admin.views.main import ChangeList


class Proposta(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    cpf = models.CharField(u'CPF', blank=True, max_length=14)
    cnpj = models.CharField(u'CNPJ', blank=True, max_length=18)
    endereco = models.CharField(u'Endereço', blank=True, null=True, max_length=255)
    bairro = models.CharField(u'Bairro', blank=True, null=True, max_length=255)
    cidade = models.CharField(u'Cidade', blank=True, null=True, max_length=255)
    estado = models.CharField(u'Estato', blank=True, null=True, max_length=2, choices=STATE_CHOICES)
    data = models.DateField(u'Data de Emissão')

    VALIDADE_CHOICES = (
        ('Quinze', '15 (Quinze)'),
        ('Trinta', '30 (Trinta)'),
        ('Sessenta', '60 (Sessenta)'),
        ('Noventa', '90 (Noventa)')
    )

    validade = models.CharField(u'Validade', blank=True, null=True, max_length=255, choices=VALIDADE_CHOICES)
    valor = models.DecimalField(u'Valor', blank=True, null=True, max_digits=8, decimal_places=2)

    CETEGORY_CHOICES = (
        ('Atrasado', 'Atrasado'),
        ('AVencer', 'Á Vencer'),
        ('Pago', 'Pago'),
    )
    situacao = models.CharField(u'Situação', blank=True, null=True, max_length=255, choices=CETEGORY_CHOICES)
    pago = models.BooleanField(default=False)

    dominio = models.CharField(u'Dominio do Site', blank=True, null=True, max_length=255,
                               help_text='URL - exe: seudomiio.com.br')
    dominio_login = models.CharField(u'Acesso ao Admin', blank=True, null=True, max_length=255,
                                     help_text='URL - exe: seudomino.com.br/admin')
    login = models.CharField(u'Login', blank=True, null=True, max_length=20)
    senha = models.CharField(u'Senha', blank=True, null=True, max_length=20)

    @property
    def imprimir(self):
        return mark_safe(""" <a href=\"/proposta/%s/\" target=\"_blank\"><img src=\"/static/proposta/img/printer.png\"></a> """  % self.id)

    class Meta:
        ordering = ['-data']
        verbose_name = 'Uma Proposta'
        verbose_name_plural = 'Propostas'

        def __str__(self) -> str:
            if self.cliente.username:
                return self.cliente.username
            else:
                return self.cliente.alias_name

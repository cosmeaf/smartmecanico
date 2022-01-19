from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created_at = models.DateTimeField('Criado', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado', auto_now=True)
    status = models.BooleanField('Situação', default=True)

    class Meta:
        abstract = True


class Endereco(models.Model):
    cep = models.CharField('Cep', max_length=8)
    logradouro = models.CharField('Logradouro', max_length=255)
    complemento = models.CharField('Complemento', max_length=255)
    bairro = models.CharField('Bairro', max_length=255)
    localidade = models.CharField('Cidade', max_length=255)
    uf = models.CharField('UF', max_length=2)

    class Meta:
        abstract = False

    def __str__(self) -> str:
        return f'{self.cep}'


class Servicos(models.Model):
    nome = models.CharField('Serviço', max_length=255)

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.nome


class Carro(models.Model):
    placa = models.CharField('Placa', max_length=8, unique=True)
    marca = models.CharField('Marca', max_length=255)
    modelo = models.CharField('Modelo', max_length=255)
    ano = models.CharField('Ano Fabricação', max_length=4)
    kilometragem = models.IntegerField('Kilometragem')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self) -> str:
        return f'{self.placa}'


class DiasVisita(models.Model):
    dia = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.dia


class HorarioAgendamento(models.Model):
    horario = models.TimeField()

    def __str__(self) -> str:
        return str(self.horario)


class Visitas(models.Model):
    choices = (('S', 'Segunda'),
               ('T', 'Terça'),
               ('Q', 'Quarta'),
               ('QI', 'Quinta'),
               ('SE', 'Sexta'),
               ('SA', 'Sabado'),
               ('D', 'Domingo'))

    choices_status = (('A', 'Agendado'),
                      ('F', 'Finalizado'),
                      ('C', 'Cancelado'))
    placa = models.ForeignKey(Carro, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dia = models.CharField(max_length=20)
    horario = models.TimeField()
    status = models.CharField(max_length=1, choices=choices_status, default="A")

    def __str__(self) -> str:
        return self.cliente.username


class Agendamento(Endereco):
    choices = (('S', 'Segunda'),
               ('T', 'Terça'),
               ('Q', 'Quarta'),
               ('QI', 'Quinta'),
               ('SE', 'Sexta'),
               ('SA', 'Sabado'),
               ('D', 'Domingo'))

    choices_status = (('A', 'Agendado'),
                      ('F', 'Finalizado'),
                      ('C', 'Cancelado'))
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    placa = models.ForeignKey(Carro, related_name='%(class)s_placa', on_delete=models.CASCADE)
    dias_visita = models.ForeignKey(DiasVisita, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField('Data Criação', auto_now_add=True)
    horarios = models.ForeignKey(HorarioAgendamento, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default="A")

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"

    def __str__(self):
        return f"{self.servico} {self.data_criacao.strftime('%d/%m/%Y')}"


class Combustivel(models.Model):
    placa = models.ForeignKey(Carro, related_name='%(class)s_placa', on_delete=models.CASCADE)
    litros = models.FloatField('Litros', blank=True, default=0.00, editable=True)
    kilometragem = models.IntegerField('Kilometragem', )
    preco = models.DecimalField('Preço Pago', max_digits=8, decimal_places=2, editable=True)
    data_compra = models.DateField()

    class Meta:
        verbose_name = 'Combustivel'
        verbose_name_plural = 'Combustiveis'

    def __str__(self) -> str:
        return f'{self.placa} {self.litros} {self.kilometragem} {self.preco} {self.data_compra}'


class Cliente(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True)
    placa = models.ForeignKey(Carro, related_name='%(class)s_placa', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self) -> str:
        return f'{self.cliente} {self.endereco} | {self.placa}'

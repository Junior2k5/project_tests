import uuid
from django.db import models
from stdimage.models import StdImageField

# Create your models here.

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Modificação', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome

class Recurso(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-laptop-phone', 'Celular'),
        ('lni-layers', 'Camadas'),
        ('lni-leaf', 'Folha'),
        ('lni-rocket', 'Foguete'),
    )

    recurso = models.CharField('Recurso', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso

class Cliente(Base):
    nome = models.CharField('Nome', max_length=100)
    empresa = models.CharField('Empresa', max_length=100)
    depoimento = models.TextField('Depoimento', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width': 75, 'height': 75, 'crop': True}})

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome

class Preco(Base):
    ICONE_CHOICES = (
        ('lni-package', 'Pacote'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela'),
    )
    plano = models.CharField('Plano', max_length=10)
    mensalidade = models.TextField('Mensalidade', max_length=40)
    quantidade = models.TextField('Quantidade de usuários', max_length=40)
    capacidade = models.TextField('Capacidade', max_length=40)
    suporte = models.TextField('Suporte', max_length=40)
    atualizacoes = models.TextField('Atualizações', max_length=40)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.plano
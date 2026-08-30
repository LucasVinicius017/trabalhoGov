from django.db import models

# Create your models here.
class Usuario(models.Model):

    PERFIL = (
        ("Administrador", "Administrador"),
        ("Usuario", "Usuário"),
    )

    STATUS = (
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),
    )

    nome = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    senha = models.CharField(
        max_length=255
    )

    perfil = models.CharField(
        max_length=20,
        choices=PERFIL,
        default="Usuario"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Ativo"
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nome

class PontoWifi(models.Model):

    STATUS = (
        ("Online", "Online"),
        ("Offline", "Offline"),
        ("Manutencao", "Em Manutenção"),
    )

    codigo = models.CharField(
        max_length=20,
        unique=True
    )

    nome = models.CharField(
        max_length=100
    )

    endereco = models.CharField(
        max_length=200
    )

    bairro = models.CharField(
        max_length=100
    )

    cidade = models.CharField(
        max_length=100
    )

    ip = models.GenericIPAddressField()

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Online"
    )

    observacao = models.TextField(
        blank=True,
        null=True
    )

    data_cadastro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Manutencao(models.Model):

    ponto = models.ForeignKey(
        PontoWifi,
        on_delete=models.CASCADE
    )

    problema = models.CharField(max_length=200)

    responsavel = models.ForeignKey(
    Usuario,
    on_delete=models.CASCADE
    )

    data_abertura = models.DateField()

    data_fechamento = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=[
            ("Aberta", "Aberta"),
            ("Em andamento", "Em andamento"),
            ("Concluída", "Concluída")
        ]
    )

    observacao = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.ponto.nome} - {self.status}"
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Plano (models.Model):

    nome = models.CharField(max_length=100)
    velocidade_download = models.IntegerField(
        help_text= "Em Mbps" #isso ajuda o usuário a como preencher o campo
    )
    velocidade_upload = models.IntegerField(
        help_text="Em Mbps"
    )
    preco_mensal = models.DecimalField (#dizem que nunca se usa float pra guardar dinheiro em django
        max_digits=10,
        decimal_places=2,
        help_text="Valor em reais (ex: 100.00)")
    ativo = models.BooleanField (default=True) #manter como padrão True, se foi criado é porque é vendido 

    def __str__(self):
        return self.nome

class Cliente (models.Model):

    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14, unique= True) #unique true cpf é único no sistema
    email = models.EmailField (unique = True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=150)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    plano = models.ForeignKey(Plano, on_delete=models.PROTECT, related_name='clientes') #protect pra impedir que alguém delete um plano que já tenha cliente usando 
    data_cadastro = models.DateTimeField(auto_now_add=True) #com esse parâmetro é preenchido automaticamente

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"

    
class Equipamento (models.Model):

    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    mac = models.CharField(max_length=17, unique=True) #todo endereço MAC de rede é único no mundo
    num_serie = models.CharField(max_length=50, unique=True)
    STATUS_CHOICES = [
        ('ESTOQUE', 'Em Estoque'),
        ('INSTALADO', 'Instalado em Cliente'),
        ('MANUTENCAO', 'Em Manutenção / Defeito'),
    ]
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default='ESTOQUE') #esse default porque todo equipamento novo já nasce em estoque
    cliente = models.ForeignKey(
        Cliente,
        null=True, 
        blank=True, 
        related_name= 'equipamentos',
        on_delete=models.SET_NULL # se o cliente for exluído, o equipamento não pode ser apagado do banco
        )

    def __str__(self):
        return f"{self.tipo} {self.modelo} - MAC: {self.mac}"

class Tecnico (models.Model):

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, #se o usuário é deletado, o perfil daquel técnico é removido junto
        related_name='tecnico',
    )
    matricula = models.CharField(max_length=20, unique=True)
    telefone =  models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.get_full_name() or self.usuario.username} (Mat: {self.matricula})"

class Chamado (models.Model):

    protocolo = models.CharField(max_length=20, unique= True)
    cliente = models.ForeignKey (
        Cliente,
        on_delete= models.CASCADE,
        related_name='chamados'
        )
    equipamento = models.ForeignKey(Equipamento,
        on_delete=models.SET_NULL, 
        null=True, 
        blank= True, 
        related_name= 'chamados',
    )
    tipo_problema = models.CharField(max_length=100)
    PRIORIDADE_CHOICES = [
            ('BAIXA', 'Baixa'),
            ('MEDIA', 'Média'),
            ('ALTA', 'Alta'),
            ('CRITICA', 'Crítica'),
        ]
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='MEDIA')
    STATUS_CHOICES = [
            ('ABERTO', 'Aberto'),
            ('EM_ANDAMENTO', 'Em Andamento'),
            ('CONCLUIDO', 'Concluído'),
            ('CANCELADO', 'Cancelado'),
        ]
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default='ABERTO')
    descricao = models.TextField()
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_conclusao = models.DateTimeField(null=True, blank= True)
    tecnicos = models.ManyToManyField(Tecnico,
        blank=True,
        related_name='chamados',
        )

    def __str__ (self):
        return f"Chamado #{self.protocolo} - {self.cliente.nome} ({self.get_status_display()})"
    
from django.db import models
from django.contrib.auth.models import User

# 🩸 Requisito 1 e 2: Registro e Previsão de Ciclo
class Ciclo(models.Model):
    data_inicio = models.DateField(verbose_name="Data de início do ciclo")
    data_proxima = models.DateField(verbose_name="Data prevista do próximo ciclo", null=True, blank=True)
    data_fim = models.DateField(verbose_name="Data de fim do ciclo", null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuária")

    def __str__(self):
        return f"Ciclo de {self.usuario.username} iniciado em {self.data_inicio}"

    class Meta:
        verbose_name = "Ciclo"
        verbose_name_plural = "Ciclos"

# 💡 Requisito 3: Dicas sobre saúde menstrual
class Dica(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da dica")
    conteudo = models.TextField(verbose_name="Conteúdo da dica")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Dica"
        verbose_name_plural = "Dicas"

# 😣 Requisito 4: Registro de sintomas
class Sintoma(models.Model):
    descricao = models.TextField(verbose_name="Descrição do sintoma")
    data = models.DateField(verbose_name="Data do registro")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuária")

    def __str__(self):
        return f"Sintoma de {self.usuario.username} em {self.data}"

    class Meta:
        verbose_name = "Sintoma"
        verbose_name_plural = "Sintomas"

class CicloMenstrual(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    ultima_menstruacao = models.DateField()
    duracao_ciclo = models.IntegerField(default=28)

    def __str__(self):
        return f"Ciclo de {self.usuario.username}"
    
class RegistroCiclo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    data_menstruacao = models.DateField()
    sintomas = models.TextField()
    atividades = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.data_menstruacao}"

from django.db import models

class Dica(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    categoria = models.CharField(max_length=50, blank=True)  # Ex: "TPM", "Cólicas", etc.
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
  

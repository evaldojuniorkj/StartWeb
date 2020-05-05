from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Questao(models.Model):
    texto_questao = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('Data Publicação')

    def publicado_recente(self):
        return self.data_publicacao >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.texto_questao


class Escolha(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto_escolha = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)
    def __str__(self):
        return self.texto_escolha
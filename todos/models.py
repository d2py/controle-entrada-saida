from django.db import models


STATUS = (
    ("R", "Retirado"),
    ("E", "Entregue"),
)


class Entradamanutencao(models.Model):
    requisicao = models.IntegerField(verbose_name="requisição", null=False, blank=False)
    ano = models.IntegerField(verbose_name="Ano", null=False, blank=False)
    local = models.CharField(
        verbose_name="Local", max_length=30, null=False, blank=False
    )
    patrimonio = models.IntegerField(verbose_name="Patrimônio", null=False, blank=False)
    solicitante = models.CharField(
        verbose_name="Solicitante", max_length=30, null=False, blank=False
    )
    equipamento = models.CharField(
        verbose_name="Equipamento", max_length=30, null=False, blank=False
    )
    dataentrada = models.DateField(
        verbose_name="Data de Entrada", null=False, blank=False
    )
    dataconclusao = models.DateField(verbose_name="Data Conclusão", null=True)
    concluido = models.CharField(verbose_name="Concluido", max_length=1, null=True)

    ret_ent = models.CharField(
        verbose_name="STATUS", max_length=1, choices=STATUS, null=True, default="------"
    )
    data_saida = models.DateField(verbose_name="Data de Saída", null=True, blank=True)
    responsavel = models.CharField(
        verbose_name="Responsavel", max_length=30, null=False, blank=False
    )
    matricula = models.IntegerField(verbose_name="Matricula", null=True, blank=False)
    retirado = models.IntegerField(verbose_name="retirado", null=True)

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
        verbose_name="Data de Entrada", null=False, blank=False, error_messages={'invalid': "Essa data não e valida"})
    
    dataconclusao = models.DateField(verbose_name="Data Conclusão", null=True)
    concluido = models.CharField(verbose_name="Concluido", max_length=1, null=True)

    
    
    
class RetiradaEquip(models.Model):   
    Equipamanto = models.ForeignKey(Entradamanutencao, on_delete=models.CASCADE)
    ret_ent = models.CharField(
        verbose_name="STATUS", max_length=1, choices=STATUS, null=False, default="------"
    )
    data_saida = models.DateField(verbose_name="Data de Saída", null=False, blank=True, error_messages={'invalid': "Essa data não e valida"})
    responsavel = models.CharField(
        verbose_name="Responsavel", max_length=30, null=False, blank=False
    )
    matricula = models.IntegerField(verbose_name="Matricula", null=False, blank=False)
    

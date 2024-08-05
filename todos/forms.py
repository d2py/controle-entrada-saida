from django import forms
from todos.models import Entradamanutencao


STATUS = (
    ("R", "Retirado"),
    ("E", "Entregue"),
)


class EntradaEquipamentoForm(forms.ModelForm):
    class Meta:
        model = Entradamanutencao

        fields = [
            "requisicao",
            "ano",
            "local",
            "patrimonio",
            "solicitante",
            "equipamento",
            "dataentrada",
        ]

    # Compos de Entrada dos Equipametos

    # Campos de Retirada


class RetiradaEquip(forms.ModelForm):
    class Meta:
        model = Entradamanutencao

        fields = [
            "requisicao",
            "ano",
            "local",
            "patrimonio",
            "solicitante",
            "equipamento",
            "dataentrada",
            "ret_ent",
            "data_saida",
            "responsavel",
            "matricula",
        ]

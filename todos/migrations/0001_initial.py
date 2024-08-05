# Generated by Django 5.0.6 on 2024-07-24 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entradamanutencao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("requisicao", models.IntegerField(verbose_name="requisição")),
                ("ano", models.IntegerField(verbose_name="Ano")),
                ("local", models.CharField(max_length=30, verbose_name="Local")),
                ("patrimonio", models.IntegerField(verbose_name="Patrimônio")),
                (
                    "solicitante",
                    models.CharField(max_length=30, verbose_name="Solicitante"),
                ),
                (
                    "equipamento",
                    models.CharField(max_length=30, verbose_name="Equipamento"),
                ),
                ("dataentrada", models.DateField(verbose_name="Data de Entrada")),
                (
                    "dataconclusao",
                    models.DateField(null=True, verbose_name="Data Conclusão"),
                ),
                (
                    "concluido",
                    models.CharField(max_length=1, null=True, verbose_name="Concluido"),
                ),
                (
                    "ret_ent",
                    models.CharField(
                        choices=[("R", "Retirado"), ("E", "Entregue")],
                        default="------",
                        max_length=1,
                        null=True,
                        verbose_name="STATUS",
                    ),
                ),
                (
                    "data_saida",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de Saída"
                    ),
                ),
                (
                    "responsavel",
                    models.CharField(max_length=30, verbose_name="Responsavel"),
                ),
                ("matricula", models.IntegerField(null=True, verbose_name="Matricula")),
                ("retirado", models.IntegerField(null=True, verbose_name="retirado")),
            ],
        ),
    ]

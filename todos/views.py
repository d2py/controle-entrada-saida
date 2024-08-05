
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse


from todos.forms import EntradaEquipamentoForm, RetiradaEquip

from .models import Entradamanutencao


# Toda a lista
def todo_list(request):
    if request.method == "GET":
        todos = Entradamanutencao.objects.all()
        return render(request, "todos/todo_list.html", {"todos": todos})


# Formulario de entrada de equipamentos
def entrada_eq(request):
    if request.method == "POST":
        form = EntradaEquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            todos = Entradamanutencao.objects.all()
            return render(request, "todos/todo_list.html", {"todos": todos})

    else:
        form = EntradaEquipamentoForm()
    return render(request, "todos/entradamanutencao_form.html", {"form": form})


"""def entradamanutencao(request):
    if request.method == "GET":
        return render(request, 'todos/entradamanutencao_form.html')
    elif request.method == "POST":
        requisicao = request.POST.get('requisicao')
        ano = request.POST.get('ano')
        local = request.POST.get('local')
        patrimonio = request.POST.get('patrimonio')
        solicitante = request.POST.get('solicitante')
        equipamento = request.POST.get('equipamento')
        dataentrada = request.POST.get('dataentrada')

        entradamanutencao = Entradamanutencao(
            requisicao = requisicao,
            ano = ano,
            local = local,
            patrimonio = patrimonio,
            solicitante = solicitante,
            equipamento = equipamento,
            dataentrada = dataentrada

        )

        entradamanutencao.save()
        return render(request, 'todos/entradamanutencao_form.html')"""


# Editar informação
def editar_infor(request, requisicao):
    if request.method == "GET":
        todos = Entradamanutencao.objects.get()
        form = EntradaEquipamentoForm, RetiradaEquip
        form = todos
        return render(request, "todos/editar_infor.html", {"form": form})


class TodoListaView(ListView):
    model = Entradamanutencao


class TodoCreateView(CreateView):
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
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
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
    success_url = reverse_lazy("toda_list_saida")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Entradamanutencao, pk=pk)
        todo.concluido = "concluido"
        todo.dataconclusao = date.today()

        todo.save()
        todos = Entradamanutencao.objects.all()
        return render(request, "todos/todo_list.html", {"todos": todos})


# Entrega de equipamentos


def lista_retirada(request):
    if request.method == "GET":

        todos = Entradamanutencao.objects.all()

        return render(request, "todos/retirada_eq.html", {"todos": todos})


"""def nova_retirada(request):       
    todos = Entradamanutencao.objects.all()
    for todo in todos:
        todo.pk
        id_pk = todo.pk
        todo_pk = Entradamanutencao.objects.get(pk=id_pk)

    entradamanutencao = get_object_or_404(Entradamanutencao, pk = todo_pk)   
    
    if request.method == 'POST':
        form = RetiradaEquip(request.POST)
        if form.is_valid():
            retirada = form.save(commit=False)
            retirada = entradamanutencao.pk
            retirada.save()       
            todos = Entradamanutencao.objects.all()
            return render(request, 'todos/retirada_eq.html', {"todos":todos})
    else:
        form = RetiradaEquip()
    return render(request, "todos/retirada_form.html", {'form': form})"""


def form_retirada(request):
    if request.method == "POST":
        form = RetiradaEquip(request.POST)

        if form.is_valid():
            form.save()
            todos = Entradamanutencao.objects.all()
            return render(request, "todos/retirada_eq.html", {"todos": todos})

    else:
        form = RetiradaEquip()
    return render(request, "todos/retirada_form.html", {"form": form})




def home(request):
    return render(request, "global/base_home.html")

def br(request):
    return render(request, "global/br.html")


def lado(request):
    return render(request, "todos/lado.html")
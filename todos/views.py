from datetime import date
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse


from todos.forms import EntradaEquipamentoForm, RetiradaEquipForm

from .models import Entradamanutencao, RetiradaEquip

# List Prohibited
def list_Prohibited(request):
    if request.method == "GET":
        list_Prohibited = Entradamanutencao.objects.all()
        return render(request, "todos/list_entrada.html", {"Prohibited": list_Prohibited})



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
            return redirect("todo_list")       
    else:
        form = EntradaEquipamentoForm()
    return render(request, "todos/entrada_eq.html", {"form": form})





# Editar informação
def editar_infor(request, pk):  
    object = get_object_or_404(Entradamanutencao, pk=pk)    
    if request.method == "POST":
        form = EntradaEquipamentoForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            todos = Entradamanutencao.objects.all()
            return render(request, "todos/todo_list.html", {"todos": todos})
    else:
        form = EntradaEquipamentoForm(instance=object)
        return render(request, "todos/editar_infor.html", {"form": form})




# Concluir um serviço
def get(request, pk):
    if request.method == "GET":
        todo = get_object_or_404(Entradamanutencao, pk=pk)
        todo.concluido = "concluido"
        todo.dataconclusao = date.today()
        todo.save()
        todos = Entradamanutencao.objects.all()
        return render(request, "todos/todo_list.html", {"todos": todos})




# Equipamentos prontos para ser entregue ao usuario 
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
        
        form = RetiradaEquipForm(request.POST)        
        if form.is_valid():             
            form.save()
            return redirect("ret")
    else:
        form = RetiradaEquipForm()
    return render(request, "todos/criar_retirada.html", {"form": form})
















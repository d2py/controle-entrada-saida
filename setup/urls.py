from django.contrib import admin
from django.urls import path
from todos import views

from todos.views import TodoCompleteView, TodoUpdateView, TodoListaView

from todos.views import todo_list, editar_infor


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListaView.as_view(), name="todo_list"),
    path("atualizar/<int:pk>", TodoUpdateView.as_view(), name="todo_atualizar"),
    path("concluir/<int:pk>", TodoCompleteView.as_view(), name="todo_concluido"),
    # TABELA DE ENTREGA
    path("list", todo_list, name="todo_list"),
    path("editar/<int:pk>", editar_infor, name="editar_infor"),
    path("ret/", views.lista_retirada, name="toda_list_saida"),
    path("form_ret/", views.form_retirada, name="saida"),
    # path('chave/', views.nova_retirada, name="chave"),
    path("entrada/", views.entrada_eq, name="entrada"),
    # path('process_formulario/', views.entradamanutencao, name='process'),
    path("home/", views.home),
    path("rb/", views.br),
    path("lado/", views.lado),
]

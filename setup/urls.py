from django.contrib import admin
from django.urls import path
from todos import views



from todos.views import todo_list, editar_infor


urlpatterns = [
    path("admin/", admin.site.urls),
    
    # TABELA DE ENTREGA
    path("list", todo_list, name="todo_list"),
    path("editar/<int:pk>", editar_infor, name="editar_infor"),
    path("ret/", views.lista_retirada, name="toda_list_saida"),
    path("form_ret/", views.form_retirada, name="saida"),
    path("entrada/", views.entrada_eq, name="entrada"),
    
    
]

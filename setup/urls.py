from django.contrib import admin
from django.urls import path
from todos import views


urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("list", views.todo_list, name="todo_list"),
    
    path("entrada/", views.entrada_eq, name="entrada"),
    path("editar/<int:pk>", views.editar_infor, name="editar_infor"),
       
    
    path("pronto/<int:pk>", views.get,name="pronto_pr" ),

    path("ret/", views.lista_retirada, name="toda_list_saida"),
    #path("retirada/<int:pk>", views.form_retirada, name="retirada"),
    path("retirada/<int:pk>", views.nova_retirada, name="retirada"),
    
]

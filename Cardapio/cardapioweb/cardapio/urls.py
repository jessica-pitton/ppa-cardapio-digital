from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("cliente/novo", views.novo, name="novo"),
    path('cliente/cadastrar', views.cadastro_cliente, name='cadastro_cliente'),
    path('cliente/pagina_sucesso/', views.pagina_sucesso, name='pagina_sucesso'),

]

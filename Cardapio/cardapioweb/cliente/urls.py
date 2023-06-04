from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.novo, name="index"),
    path("novo", views.novo, name="novo"),
    path('cadastrar', views.cadastro_cliente, name='cadastro_cliente'),
    path('pagina_sucesso', views.pagina_sucesso, name='pagina_sucesso'),

]

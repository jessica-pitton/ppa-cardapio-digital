from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.cadastro_cliente, name="index"),
    path('cadastrar', views.cadastro_cliente, name='cadastro_cliente'),
    path('pagina_sucesso', views.pagina_sucesso, name='pagina_sucesso'),

]

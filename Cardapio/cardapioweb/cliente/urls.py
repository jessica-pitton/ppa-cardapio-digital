from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('pagina_sucesso', views.pagina_sucesso, name='pagina_sucesso'),

]

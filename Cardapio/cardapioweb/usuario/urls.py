from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('logar_usuario', views.logar_usuario, name="logar_usuario"),
    path('logout', views.logout_user, name="logout"),
    path('cadastrar_usuario', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('index', views.index, name="index"),
]
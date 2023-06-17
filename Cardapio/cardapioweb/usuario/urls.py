from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login', views.realizar_login, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('cadastrar_usuario', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('index', views.index, name="index"),
]
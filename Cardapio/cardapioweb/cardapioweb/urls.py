from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path("cliente/", include("cliente.urls")),
    path("funcionario/", include("funcionario.urls")),
    path("", include("produto.urls")),
    path("pedido/", include("pedido.urls")),
    path("usuario/", include("usuario.urls")),
    path('admin/', admin.site.urls),
]

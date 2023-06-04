from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path("cliente/", include("cliente.urls")),
    path('admin/', admin.site.urls),
]

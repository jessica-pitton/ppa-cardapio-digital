from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    path("cardapio/", include("cardapio.urls")),
    path('admin/', admin.site.urls),
]

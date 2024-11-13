"""
URL configuration for biblioteca_citas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from citas.views import lista_citas, crear_cita, editar_cita, eliminar_cita, crear_fuente

urlpatterns = [
    path('', lista_citas, name=''),
    path('crear_cita', crear_cita, name='crear_cita'),
    path('editar_cita', editar_cita, name='editar_cita'),
    path('eliminar_cita', eliminar_cita, name='eliminar_cita'),
    path('crear_fuente', crear_fuente, name='crear_fuente'),
]

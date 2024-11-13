from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Cita
from django.db.models import Q

def lista_citas(request):
    # Obtenemos las citas con filtros aplicados
    citas = Cita.objects.all()

    # Filtros
    autor = request.GET.get('autor', '')
    tipo_fuente = request.GET.get('tipo_fuente', '')
    año = request.GET.get('año', '')

    if autor:
        citas = citas.filter(autor__icontains=autor)  # Filtro por autor (buscar parcial)
    
    if tipo_fuente:
        citas = citas.filter(fuente__tipo__icontains=tipo_fuente)  # Filtro por tipo de fuente
    
    if año:
        citas = citas.filter(fecha__year=año)  # Filtro por año

    # Paginación: Mostrar 5 citas por página
    paginator = Paginator(citas, 5)
    page_number = request.GET.get('page')  # Obtiene el número de la página de la URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'citas/lista_citas.html', {'page_obj': page_obj, 'autor': autor, 'tipo_fuente': tipo_fuente, 'año': año})
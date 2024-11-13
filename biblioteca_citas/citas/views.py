from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Cita, Fuente
from django.db.models import Q

# Vista para la Lista de Citas con Paginación y Filtros
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

# Vista para Crear una Nueva Cita
def crear_cita(request):
    if request.method == 'POST':
        texto = request.POST.get('texto')
        autor = request.POST.get('autor')
        fecha = request.POST.get('fecha')
        fuente_id = request.POST.get('fuente')
        
        fuente = Fuente.objects.get(id=fuente_id)
        Cita.objects.create(texto=texto, autor=autor, fecha=fecha, fuente=fuente)
        return redirect('lista_citas')  # Redirige a la lista de citas después de crear una cita

    fuentes = Fuente.objects.all()
    return render(request, 'citas/crear_cita.html', {'fuentes': fuentes})

# Vista para Editar una Cita
def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)

    if request.method == 'POST':
        cita.texto = request.POST.get('texto')
        cita.autor = request.POST.get('autor')
        cita.fecha = request.POST.get('fecha')
        fuente_id = request.POST.get('fuente')
        cita.fuente = Fuente.objects.get(id=fuente_id)
        cita.save()

        return redirect('lista_citas')  # Redirige a la lista de citas después de editar

    fuentes = Fuente.objects.all()
    return render(request, 'citas/editar_cita.html', {'cita': cita, 'fuentes': fuentes})

# Vista para Eliminar una Cita
def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)

    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')  # Redirige a la lista de citas después de eliminar la cita
    
    return render(request, 'citas/eliminar_cita.html', {'cita': cita})

# Vista para Crear una Nueva Fuente
def crear_fuente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')

        Fuente.objects.create(nombre=nombre, tipo=tipo)
        return redirect('lista_citas')  # Redirige a la lista de citas después de crear una fuente

    return render(request, 'citas/crear_fuente.html')
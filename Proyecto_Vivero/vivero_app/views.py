from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Productor

# Create your views here.
def productor_detail(request, productor_id):
    try:
        productor = Productor.objects.get(Documento=productor_id)
        return render(request, 'productor_detail.html', {'productor': productor})
    except Productor.DoesNotExist:
        # Si no se encuentra el productor, renderiza la misma plantilla con un mensaje de error
        error_message = f"No se encontró ningún productor con el Documento {productor_id}."
        return render(request, 'productor_detail.html', {'error_message': error_message})
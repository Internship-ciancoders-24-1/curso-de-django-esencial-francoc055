from django.http import HttpResponse
from datetime import datetime
import json

def saludar(request):
    now = datetime.now().strftime('%Y %b %dth - %H:%M hrs')
    return HttpResponse(f'hora: {str(now)}')

def ordenar(request):
    lista = [int(i) for i in request.GET['numeros'].split(',')]
    lista.sort()
    numbers = {"numbers": lista}
    return HttpResponse(json.dumps(numbers), content_type='application/json')
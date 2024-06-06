from django.http import JsonResponse
from .models import Curso

def index(request):
    context={
        'status': True,
        'content': 'API con Django'
    }
    return JsonResponse(context)

def curso(request):
    cursos = Curso.objects.all()
    
    context= {
        'status': True,
        'content': list(cursos.values())
    }
    return JsonResponse(context)
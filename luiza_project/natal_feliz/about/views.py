from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import HttpResponse

membros = [
    {
        'nome':'Isadora',
        'job':'Masters student',
        'job_comp':'USP',
        'job-loc':'SP-Brazil'
    },
    {
        'nome':'Regina',
        'job':'Software Engineer',
        'job_comp':'Gama',
        'job_loc':'SP-Brazil'
    }
]

# Create your views here.
def home(request):
    contexto = {
        'membros':membros,
        'titulo':"Shopping de natal"

    } 
    return render(request, 'home.html',contexto)


def about(request):
    return HttpResponse("<h1>Site sobre coisinhas de Natal</h1>")
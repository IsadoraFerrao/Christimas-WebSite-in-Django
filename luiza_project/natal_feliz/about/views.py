from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Bem-vindo ao incrível site de coisinhas de Natal :) </h1>")
def about(request):
    return HttpResponse("<h1>Site sobre coisinhas de Natal</h1>")
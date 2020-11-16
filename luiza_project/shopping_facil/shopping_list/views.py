from django.shortcuts import render
from django.http import HttpRequest
from django.http.response import HttpResponse

def home(request):
    return HttpResponse("<h1>Shopping da Isa</h1>")

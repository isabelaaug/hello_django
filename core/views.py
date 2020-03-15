from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos </h1>')  # http://127.0.0.1:8000/hello/Isa/24

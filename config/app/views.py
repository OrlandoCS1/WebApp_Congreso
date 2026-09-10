from django.shortcuts import render
from app.forms import UsuarioForm


# Create your views here.

def base(request):
    return render(request, 'app/base.html')

def home(request):
    return render(request, 'app/pages/home.html')

def evaluador(request):
    return render(request, 'app/pages/evaluador.html')

def form_usuarios(request):
    formulario = UsuarioForm()
    contexto = {'formulario': formulario}
    return render(request, 'crear_usuarios.html', contexto)






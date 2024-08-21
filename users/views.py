from django.shortcuts import render, redirect
from .models import persona
from .form import personaForm

# Create your views here.


def listar_personas(request):
    personas = persona.objects.all()
    return render(request,'listarUsuario.html',{'personas':personas})

def crear_persona(request):
    if request.method == 'POST':
        form = personaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(listar_personas)
    else:
        form = personaForm()
        return render(request,'crear_persona.html',{'form':form})
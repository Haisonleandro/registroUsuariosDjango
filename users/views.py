from django.shortcuts import render, redirect
from .models import persona
from .form import personaForm

# Create your views here.


def registerUser(request):
    if request.method == 'POST':
        form = personaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarUsuario')
        
    else:
        form = personaForm()
    return render(request,'registroUsuario.html',{'form':form})

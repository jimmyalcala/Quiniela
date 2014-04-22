from django.shortcuts import render_to_response
from django.template import RequestContext
from quiniela.apps.champions.models import UserProfile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
import random
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.db.models import Max
from quiniela.apps.champions.forms import Upload,QuinielaForm
from quiniela.apps.champions.models import Paises,Grupos,Niveles,Equipos, CalendarioFase, Fechas, FaseDeGrupos, Quiniela, CalendarioOctavos, CalendarioCuartos
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from quiniela.apps.champions.aletorio import aleatorio

def usuarios_view(request):
    usuarios=UserProfile.objects.filter(tipoPerfil="jugador").order_by('-puntos')
    ctx={'usuarios':usuarios}
    return render_to_response('usuarios.html',ctx,context_instance=RequestContext(request))

def crearUsuario_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            nombre=request.POST['username']
            form.save()
            usuario=User.objects.aggregate(Max('id'))
            ide=usuario['id__max']
            cliente=UserProfile()
            cliente.usuario_id=ide
            cliente.nombre=nombre
            cliente.tipoPerfil_id="jugador"
            cliente.save()
            return HttpResponseRedirect("../")
    else: 
        form=UserCreationForm()
    ctx={'form':form}
    return render_to_response('registro.html',ctx,context_instance=RequestContext(request))

def crearUsuarioAdmin_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
        if tipo2 == "administrador":
            if request.method=='POST':
                form=UserCreationForm(request.POST)
                if form.is_valid():
                    nombre=request.POST['username']
                    form.save()
                    usuario=User.objects.aggregate(Max('id'))
                    ide=usuario['id__max']
                    cliente=UserProfile()
                    cliente.usuario_id=ide
                    cliente.nombre=nombre
                    cliente.tipoPerfil_id="administrador"
                    cliente.save()
                    return HttpResponseRedirect("../")
            else: 
                form=UserCreationForm()
            ctx={'form':form}
            return render_to_response('registroAdmin.html',ctx,context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect("../")
    else:
        return HttpResponseRedirect("../")


def ingresar_view(request):
    mensaje="todo bien"
    if request.user.is_authenticated():
        return HttpResponseRedirect("../")
    else:
        if request.method=="POST":
            form=AuthenticationForm(request.POST)
            if form.is_valid():
                print "valido"
            else:
                username=request.POST['username']
                password=request.POST['password']
                usuario=authenticate(username=username,password=password)
                if usuario is not None:
                    login(request,usuario)
                    return HttpResponseRedirect("../")
                else:
                    mensaje="usuario y o pass incorrecto"
        else: 
            form=AuthenticationForm()
        ctx={'form':form,'mensaje':mensaje}
        return render_to_response('ingresar.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return render_to_response('adios.html',context_instance=RequestContext(request)) 




# Create your views here.

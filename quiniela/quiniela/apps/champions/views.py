from django.shortcuts import render_to_response
from django.template import RequestContext
from quiniela.apps.champions.models import UserProfile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
import random
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.db.models import Max
from quiniela.apps.champions.forms import Upload,QuinielaFormFinal,nombreForm
from quiniela.apps.champions.models import Paises,Grupos,Niveles,Equipos, CalendarioFase, Fechas, FaseDeGrupos, Quiniela, CalendarioOctavos, CalendarioCuartos
from quiniela.apps.champions.models import UserProfile,QuinielaOctavos, QuinielaCuartos, QuinielaSemi, QuinielaFinal,Verificacion
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from quiniela.apps.champions.aletorio import aleatorio
from django.db.models import Q







def carga_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    tipo="TXT"
    lista={}
    veri1=Verificacion.objects.all()
    if veri1:
        return render_to_response('errorCarga.html',context_instance=RequestContext(request))
    else:
        if request.method=="POST":
            form=Upload(request.POST)
            if form.is_valid():
                    nombre=form.cleaned_data['nombre']
                    try: 
                        f= open('quiniela/media/archivos/'+nombre+'.txt','r')
                    except:
                        return render_to_response('errorCarga.html',context_instance=RequestContext(request))
                    lns = f.readlines()
                    i=0  
                    for line in lns:          
                        line=line.split('|')
                        if len(line)>9:
                            return render_to_response('errorCarga.html',context_instance=RequestContext(request))
                        i=i+1
                            #hacer operaciones     
                        lista[i]={'grupo':line[0],'grupo2':line[1],'nivel':line[2],'pais':line[3],'pais2':line[4],'pais3':line[5],'pais4':line[6],'pais5':line[7],'tete':line[8]}
                        a=Grupos()
                        b=Paises()
                        c=Niveles()
                        a.numeroGrupo=lista[i]['grupo']
                        a.save()
                        a2=Grupos()
                        a2.numeroGrupo=lista[i]['grupo2']
                        a2.save()
                        c.level=int(lista[i]['nivel'])
                        c.save()
                        b.nacionalidad=lista[i]['pais']
                        b.save()
                        b1=Paises()
                        b1.nacionalidad=lista[i]['pais2']
                        b1.save()
                        b2=Paises()
                        b2.nacionalidad=lista[i]['pais3']
                        b2.save()
                        b3=Paises()
                        b3.nacionalidad=lista[i]['pais4']
                        b3.save()
                        b4=Paises()
                        b4.nacionalidad=lista[i]['pais5']
                        b4.save()
                    f.close()
                    veri=Verificacion()
                    veri.registro=1
                    veri.save()         
                    informacion=" Se cargo correctamente el archivo a la base de datos "
                    ctx={'informacion':informacion,'tipo2':tipo2}
                    return render_to_response('respuesta.html',ctx,context_instance=RequestContext(request)) 
            else:
                form=Upload()
                informacion="No se guardo correctamente el archivo en la base de datos"
                ctx={'form':form,'informacion':informacion,'tipo':tipo,'tipo2':tipo2}
                return render_to_response('carga.html',ctx,context_instance=RequestContext(request))  
        else:
            form=Upload()
            ctx={'form':form,'tipo':tipo,'tipo2':tipo2}
            return render_to_response('carga.html',ctx,context_instance=RequestContext(request))
        
def carga2_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    tipo="TXT"
    lista={}
    regi=0
    veri1=Verificacion.objects.filter(registro=1)
    for a in veri1:
        regi=a.registro
    if regi==1:            
        if request.method=="POST":
            form=Upload(request.POST)
            if form.is_valid():
                    nombre=form.cleaned_data['nombre']
                    try: 
                        f= open('quiniela/media/archivos/'+nombre+'.txt','r')
                    except:
                        return render_to_response('errorCarga.html',context_instance=RequestContext(request))
                    lns = f.readlines()
                    i=0  
                    for line in lns:          
                        line=line.split('|')
                        if len(line)>5:
                            return render_to_response('errorCarga.html',context_instance=RequestContext(request))
                        i=i+1
                            #hacer operaciones     
                        lista[i]={'equipo':line[0],'pais':line[1],'nivel':line[2],'grupo':line[3]}
                        a=Equipos()
                        b=FaseDeGrupos()
                        a.pais_id=lista[i]['pais']
                        a.grupo_id=lista[i]['grupo']
                        a.nivel_id=lista[i]['nivel']
                        a.club=lista[i]['equipo']
                        a.save()
                        b.nombreClub_id=lista[i]['equipo']
                        b.numeroGrupo_id=lista[i]['grupo']
                        b.save()
                    f.close()
                    veri=Verificacion.objects.filter(registro=1)
                    for q in veri:
                        q.registro=2
                        q.save()         
                    informacion=" Se cargo correctamente el archivo a la base de datos "
                    ctx={'informacion':informacion,'tipo2':tipo2}
                    return render_to_response('respuesta.html',ctx,context_instance=RequestContext(request)) 
            else:
                form=Upload()
                informacion="No se guardo correctamente el archivo en la base de datos"
                ctx={'form':form,'informacion':informacion,'tipo':tipo,'tipo2':tipo2}
                return render_to_response('carga2.html',ctx,context_instance=RequestContext(request))  
        else:
            form=Upload()
            ctx={'form':form,'tipo':tipo,'tipo2':tipo2}
            return render_to_response('carga2.html',ctx,context_instance=RequestContext(request))
    else:
        return render_to_response('errorCarga.html',context_instance=RequestContext(request))
def carga3_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    tipo="TXT"
    lista={}
    regi=0
    veri1=Verificacion.objects.filter(registro=2)
    for a in veri1:
        regi=a.registro
    if regi==2:
        if request.method=="POST":
            form=Upload(request.POST)
            if form.is_valid():
                    nombre=form.cleaned_data['nombre']
                    try: 
                        f= open('quiniela/media/archivos/'+nombre+'.txt','r')
                    except:
                        return render_to_response('errorCarga.html',context_instance=RequestContext(request))
                    lns = f.readlines()
                    i=0  
                    for line in lns:          
                        line=line.split('|')
                        if len(line)>4:
                            return render_to_response('errorCarga.html',context_instance=RequestContext(request))
                        i=i+1
                            #hacer operaciones     
                        lista[i]={'equipo1':line[0],'fecha':line[1],'equipo2':line[2]}
                        a=Fechas()
                        b=CalendarioFase()                    
                        a.date=lista[i]['fecha']
                        a.save()
                        b.fecha_id=lista[i]['fecha']
                        b.equipo1_id=lista[i]['equipo1']
                        b.equipo2_id=lista[i]['equipo2'] 
                        b.save()
                        
                    f.close()       
                    veri=Verificacion.objects.filter(registro=2)
                    for q in veri:
                        q.registro=3
                        q.save()      
                    informacion=" Se cargo correctamente el archivo a la base de datos "
                    ctx={'informacion':informacion,'tipo2':tipo2}
                    return render_to_response('respuesta.html',ctx,context_instance=RequestContext(request)) 
            else:
                form=Upload()
                informacion="No se guardo correctamente el archivo en la base de datos"
                ctx={'form':form,'informacion':informacion,'tipo':tipo,'tipo2':tipo2}
                return render_to_response('carga3.html',ctx,context_instance=RequestContext(request))  
        else:
            form=Upload()
            ctx={'form':form,'tipo':tipo,'tipo2':tipo2}
            return render_to_response('carga3.html',ctx,context_instance=RequestContext(request))
    else:
        return render_to_response('errorCarga.html',context_instance=RequestContext(request))
def ActualizarPuntos_view(request):
    puntaje=0
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
        if tipo3 == "jugador":
            return HttpResponseRedirect('../')
        else:
            usuario=UserProfile.objects.all().order_by('usuario')
            quini=Quiniela.objects.all().order_by('nombreUsuario')
            calen=CalendarioFase.objects.all()
            
            for u in usuario:    
                for x2 in quini:
                    if u.usuario==x2.nombreUsuario:
                        for x3 in calen:
                            if x3.ide==x2.iden_id:
                                if x3.gol1>x3.gol2 and x2.gol1>x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol2>x3.gol1 and x2.gol2>x2.gol1:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol1==x3.gol2 and x2.gol1==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                if x3.gol1==x2.gol1 and x3.gol2==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+3
                                
                u.puntos=puntaje
                u.save()
                puntaje=0
            mensaje3="Su simulacion ha sido realizada exitosamente"
            ctx={'puntos':puntaje,'mensaje3':mensaje3,'tipo2':tipo2}
        return render_to_response('notificacion.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')

def ActualizarPuntos8_view(request):
    puntaje=0
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "jugador":
            return HttpResponseRedirect('../')
        else:
            usuario=UserProfile.objects.all().order_by('usuario')
            quini=QuinielaOctavos.objects.all().order_by('nombreUsuario')
            calen=CalendarioOctavos.objects.all()
            for u in usuario:    
                for x2 in quini:
                    print u.usuario,x2.nombreUsuario
                    if u.usuario==x2.nombreUsuario:
                        for x3 in calen:
                            if x3.ide==x2.iden_id:
                                if x3.gol1>5 or x3.gol2>5:
                                    if x3.gol1>x3.gol2:
                                        x3.gol1=x3.gol1-6
                                        x3.gol2=x3.gol2-5
                                    else:
                                        x3.gol1=x3.gol1-5
                                        x3.gol2=x3.gol2-6

                                if x3.gol1>x3.gol2 and x2.gol1>x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol2>x3.gol1 and x2.gol2>x2.gol1:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol1==x3.gol2 and x2.gol1==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                if x3.gol1==x2.gol1 and x3.gol2==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+3
                print u.puntos,puntaje
                u.puntos=u.puntos+puntaje
                
                u.save()
                puntaje=0
            mensaje3="Su simulacion ha sido realizada exitosamente"
            ctx={'puntos':puntaje,'mensaje3':mensaje3,'tipo2':tipo2}
        return render_to_response('notificacion.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')

def ActualizarPuntos4_view(request):
    puntaje=0
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "jugador":
            return HttpResponseRedirect('../')
        else:
            usuario=UserProfile.objects.all().order_by('usuario')
            quini=QuinielaCuartos.objects.all().order_by('nombreUsuario')
            calen=CalendarioCuartos.objects.all()[:8]
            for u in usuario:    
                for x2 in quini:
                    print u.usuario,x2.nombreUsuario
                    if u.usuario==x2.nombreUsuario:
                        for x3 in calen:
                            if x3.ide==x2.iden_id:
                                if x3.gol1>5 or x3.gol2>5:
                                    if x3.gol1>x3.gol2:
                                        x3.gol1=x3.gol1-6
                                        x3.gol2=x3.gol2-5
                                    else:
                                        x3.gol1=x3.gol1-5
                                        x3.gol2=x3.gol2-6

                                if x3.gol1>x3.gol2 and x2.gol1>x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol2>x3.gol1 and x2.gol2>x2.gol1:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol1==x3.gol2 and x2.gol1==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                if x3.gol1==x2.gol1 and x3.gol2==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+3
                print u.puntos,puntaje
                u.puntos=u.puntos+puntaje
                
                u.save()
                puntaje=0
            mensaje3="Su simulacion ha sido realizada exitosamente"
            ctx={'puntos':puntaje,'mensaje3':mensaje3,'tipo2':tipo2}
        return render_to_response('notificacion.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')

def ActualizarPuntos2_view(request):
    puntaje=0
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "jugador":
            return HttpResponseRedirect('../')
        else:
            usuario=UserProfile.objects.all().order_by('usuario')
            quini=QuinielaSemi.objects.all().order_by('nombreUsuario')
            calen=CalendarioCuartos.objects.all()[8:12]
            for u in usuario:    
                for x2 in quini:
                    print u.usuario,x2.nombreUsuario
                    if u.usuario==x2.nombreUsuario:
                        for x3 in calen:
                            if x3.ide==x2.iden_id:
                                if x3.gol1>5 or x3.gol2>5:
                                    if x3.gol1>x3.gol2:
                                        x3.gol1=x3.gol1-6
                                        x3.gol2=x3.gol2-5
                                    else:
                                        x3.gol1=x3.gol1-5
                                        x3.gol2=x3.gol2-6

                                if x3.gol1>x3.gol2 and x2.gol1>x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol2>x3.gol1 and x2.gol2>x2.gol1:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol1==x3.gol2 and x2.gol1==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                if x3.gol1==x2.gol1 and x3.gol2==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+3
                print u.puntos,puntaje
                u.puntos=u.puntos+puntaje
                u.save()
                puntaje=0
            mensaje3="Su simulacion ha sido realizada exitosamente"
            ctx={'puntos':puntaje,'mensaje3':mensaje3,'tipo2':tipo2}
        return render_to_response('notificacion.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')

def ActualizarPuntos1_view(request):
    puntaje=0
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "jugador":
            return HttpResponseRedirect('../')
        else:
            usuario=UserProfile.objects.all().order_by('usuario')
            quini=QuinielaFinal.objects.all().order_by('nombreUsuario')
            calen=CalendarioCuartos.objects.all()[12:]
            for u in usuario:    
                for x2 in quini:
                    print u.usuario,x2.nombreUsuario
                    if u.usuario==x2.nombreUsuario:
                        for x3 in calen:
                            if x3.ide==x2.iden_id:
                                if x3.gol1>5 or x3.gol2>5:
                                    if x3.gol1>x3.gol2:
                                        x3.gol1=x3.gol1-6
                                        x3.gol2=x3.gol2-5
                                    else:
                                        x3.gol1=x3.gol1-5
                                        x3.gol2=x3.gol2-6
                                if x3.gol1>x3.gol2 and x2.gol1>x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol2>x3.gol1 and x2.gol2>x2.gol1:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                elif x3.gol1==x3.gol2 and x2.gol1==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+2
                                if x3.gol1==x2.gol1 and x3.gol2==x2.gol2:
                                    if x2.gol1!=None:
                                        puntaje=puntaje+3
             
                u.puntos=u.puntos+puntaje
                u.save()
                puntaje=0
                mensaje3="Su simulacion ha sido realizada exitosamente"
            ctx={'puntos':puntaje,'mensaje3':mensaje3,'tipo2':tipo2}
        return render_to_response('notificacion.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')

def VistaGrupos_view(request,pagina):
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    vista=FaseDeGrupos.objects.all().order_by('numeroGrupo','-puntos','-golesFavor')
    paginator=Paginator(vista,4)
    try:
        page=int(pagina)
    except:
        page=1
    try:
        vistaPaginada=paginator.page(page)
    except (EmptyPage,InvalidPage):
        vistaPaginada=paginator.page(paginator.num_pages)
    ctx={'grupos':vistaPaginada,'tipo2':tipo2}
    return render_to_response('Grupos.html',ctx,context_instance=RequestContext(request))


def VistaGrupos2_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    vista=Equipos.objects.filter(club="Zenit")
    ctx={'vista':vista,'tipo2':tipo2}
    return render_to_response('Grupos1.html',ctx,context_instance=RequestContext(request))

def index_view(request):
    x1=""
    mensaje=""
    tipo2=""
    usuario=""
    campeon=""
    if request.method=='POST':
        form=nombreForm(request.POST)
        if form.is_valid():
            nombre=request.POST['equip']
            equipo=Equipos.objects.filter(club=nombre)
            ctx={'equipo':equipo}
            return render_to_response('equipoFav1.html',ctx,context_instance=RequestContext(request))
    else: 
        form=nombreForm()
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1: 
            tipo2=x.tipoPerfil.tipo
        if tipo2 == "administrador":
            mensaje="eres un administrador"
        elif tipo2=="jugador":
            mensaje="eres un pobre huevon"
        print x1
    vista=CalendarioCuartos.objects.all()[12:]
    for q in vista:
        if q.gol1!=None:
            if q.gol1>q.gol2:
                campeon=q.equipo1
            else:
                campeon=q.equipo2
            usuario=UserProfile.objects.filter(tipoPerfil='jugador').order_by('-puntos')[:1]
    vista2=CalendarioOctavos.objects.all()[:8]
    vista4=CalendarioCuartos.objects.all()[8:10]
    vista3=CalendarioCuartos.objects.all()[:4]
    vista1=Equipos.objects.all().order_by('pais')
    vista5=CalendarioCuartos.objects.all()[12:]
    ctx={'form':form,"x1":x1,"mensaje":mensaje,'tipo2':tipo2,'usuario':usuario,'campeon':campeon,'vista1':vista1,'vista2':vista2,'vista3':vista3,'vista4':vista4,'vista5':vista5}
    return render_to_response('index.html',ctx,context_instance=RequestContext(request))


def VistaJuegos_view(request,nombreClub):
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    vista=CalendarioFase.objects.filter(Q(equipo1=nombreClub) | Q(equipo2=nombreClub)).order_by('ide')
    ctx={'vista':vista,'tipo2':tipo2}
    return render_to_response('EquipoFav.html',ctx,context_instance=RequestContext(request))

def vistaCarga_view(request):
    return render_to_response('vistaCarga.html',context_instance=RequestContext(request))

def vistaPuntos_view(request):
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "jugador":
            ctx={'x1':x1,'tipo2':tipo2}
            return render_to_response('puntos.html',ctx,context_instance=RequestContext(request))
        
def vistaQuinielas_view(request):
    return render_to_response('vistaQuiniela.html',context_instance=RequestContext(request))

def VistaCalendarioF_view(request):
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    vista=CalendarioFase.objects.all().order_by('ide')
    p="Fase de Grupos"
    ctx={'vista':vista,'p':p,'tipo2':tipo2}
    return render_to_response('calen.html',ctx,context_instance=RequestContext(request))

def VistaCalendarioOctavos_view(request):
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    vista=CalendarioOctavos.objects.all().order_by('juego')
    p="Octavos de Final"
    ctx={'vista':vista,'p':p,'tipo2':tipo2}
    return render_to_response('calen.html',ctx,context_instance=RequestContext(request))


def VistaCalendarioCuartos_view(request):
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    vista=CalendarioCuartos.objects.all().order_by('juego')[:8]
    p="Cuartos de Final"
    ctx={'vista':vista,'p':p,'tipo2':tipo2}
    return render_to_response('calen.html',ctx,context_instance=RequestContext(request))

def VistaCalendarioFinal_view(request):
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    vista=CalendarioCuartos.objects.all().order_by('juego')[12:]
    p="Final"
    ctx={'vista':vista,'p':p,'tipo2':tipo2}
    return render_to_response('calen.html',ctx,context_instance=RequestContext(request))

def VistaCalendarioSemi_view(request):
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    vista=CalendarioCuartos.objects.all().order_by('juego')[8:12]
    p="Semi Final"
    ctx={'vista':vista,'p':p,'tipo2':tipo2}
    return render_to_response('calen.html',ctx,context_instance=RequestContext(request))

def menuCalendario_view(request):
    tipo2=""
    veri=Verificacion.objects.filter(registro=3)
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
    regi=0
    tipo3=""
    x1=""
    for v in veri:
        regi=v.registro
    if regi==3:    
        faseG="NO"
        fase1="NO"
        fase2="NO"
        fase4="NO"
        fase8="NO"
        if request.user.is_authenticated():
            nombre=request.user
            tipo=nombre.id
            x1=UserProfile.objects.filter(usuario=tipo)
            for x in x1:
                tipo3=x.tipoPerfil.tipo
        fase=CalendarioFase.objects.all()
        for o in fase:
            if o.gol1==None:
                faseG="SI"
                break
            else:
                faseG="NO"
                cale=CalendarioOctavos.objects.all()
                for q in cale:
                    if q.gol1==None:
                        fase8="SI"
                        break
                    else:
                        fase8="NO"
                        cale2=CalendarioCuartos.objects.all()[:8]
                        for p in cale2:
                            if p.gol1==None:
                                fase4="SI"
                                break
                            else:
                                fase4="NO"
                                cale3=CalendarioCuartos.objects.all()[8:12]
                                for r in cale3:
                                    if r.gol1==None:
                                        fase2="SI"
                                        break
                                    else:
                                        fase2="NO"
                                        cale5=CalendarioCuartos.objects.all()[12:]
                                        for t in cale5:
                                            if t.gol1==None:
                                                fase1="SI"
                                                break
                                            else:
                                                fase1="SI"
                                                break
                                        break
                                break
                        break
                break
        ctx={'tipo':tipo3,'fase1':fase1,'fase2':fase2,'fase4':fase4,'fase8':fase8,'faseG':faseG,'x1':x1,'tipo2':tipo2}
        return render_to_response('menuCale.html',ctx,context_instance=RequestContext(request))  
    else:
        return HttpResponseRedirect('../')
    
def Instrucciones_view(request):
    tipo=""
    tipo2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo1=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo1)
        for x in x1:
            tipo=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
    ctx={'tipo':tipo,'tipo2':tipo2}
    return render_to_response('instrucciones.html',ctx,context_instance=RequestContext(request))
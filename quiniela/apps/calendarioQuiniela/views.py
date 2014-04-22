from django.shortcuts import render_to_response
from django.template import RequestContext
from quiniela.apps.champions.models import UserProfile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
import random
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.db.models import Max
from quiniela.apps.champions.forms import Upload,QuinielaForm,Quiniela2Form,Quiniela1Form,QuinielaForm4,modificarForm
from quiniela.apps.champions.models import Paises,Grupos,Niveles,Equipos, CalendarioFase, Fechas, FaseDeGrupos, Quiniela, CalendarioOctavos, CalendarioCuartos,QuinielaOctavos,QuinielaCuartos
from quiniela.apps.champions.models import QuinielaSemi,QuinielaFinal,Verificacion
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from quiniela.apps.champions.aletorio import aleatorio


def hacerQuiniela_view(request):
    x1=""
    x2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        print tipo3
        if tipo3 == "administrador":
            print "hola"
        else:
            us=Quiniela.objects.filter(nombreUsuario=tipo)
            if us:
                return render_to_response('error.html',context_instance=RequestContext(request))
            else:
                x2=CalendarioFase.objects.all()
                for z in x2:
                    a=Quiniela()
                    a.nombreUsuario_id=tipo
                    a.iden_id=z.ide
                    a.equipo1_id=z.equipo1_id
                    a.equipo2_id=z.equipo2_id
                    a.fecha_id=z.fecha_id
                    a.save()
            ctx={'tipo2':tipo2}
            return render_to_response('rellenaQuinielas.html',ctx,context_instance=RequestContext(request))  
    else:
        return HttpResponseRedirect("../")
    
def hacerQuiniela8_view(request):
    x1=""
    x2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        print tipo3
        if tipo3 == "administrador":
            print "hola"
        else:
            us=QuinielaOctavos.objects.filter(nombreUsuario=tipo)
            if us:
                return render_to_response('error.html',context_instance=RequestContext(request))
            x2=CalendarioOctavos.objects.all()
            for z in x2:
                a=QuinielaOctavos()
                a.nombreUsuario_id=tipo
                a.iden_id=z.ide
                a.equipo1_id=z.equipo1_id
                a.equipo2_id=z.equipo2_id
                a.fecha_id=z.fecha_id
                a.save()
        ctx={'tipo2':tipo2}
        return render_to_response('rellenaQuinielasOctavos.html',ctx,context_instance=RequestContext(request)) 
    else:
        return HttpResponseRedirect("../")    
    
def hacerQuiniela4_view(request):
    x1=""
    x2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
        print tipo3
        if tipo3 == "administrador":
            print "hola"
        else:
            us=QuinielaCuartos.objects.filter(nombreUsuario=tipo)
            if us:
                return render_to_response('error.html',context_instance=RequestContext(request))
            x2=CalendarioCuartos.objects.all()
            for z in x2:
                a=QuinielaCuartos()
                a.nombreUsuario_id=tipo
                a.iden_id=z.ide
                a.equipo1_id=z.equipo1_id
                a.equipo2_id=z.equipo2_id
                a.fecha_id=z.fecha_id
                a.save()
        return HttpResponseRedirect("/quinielaUsuario4")  
    else:
        return HttpResponseRedirect("../")        

def hacerQuiniela2_view(request):
    x1=""
    x2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
        print tipo3
        if tipo3 == "administrador":
            print "hola"
        else:
            us=QuinielaCuartos.objects.filter(nombreUsuario=tipo)[8:]
            if us:
                return render_to_response('error.html',context_instance=RequestContext(request))
            x2=CalendarioCuartos.objects.all()[8:]
            for z in x2:
                a=QuinielaSemi()
                a.nombreUsuario_id=tipo
                a.iden_id=z.ide
                a.equipo1_id=z.equipo1_id
                a.equipo2_id=z.equipo2_id
                a.fecha_id=z.fecha_id
                a.save()
        return HttpResponseRedirect("/quinielaUsuario2")  
    else:
        return HttpResponseRedirect("../") 
    
def hacerQuiniela1_view(request):
    x1=""
    x2=""
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        print tipo
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
        print tipo3
        if tipo3 == "administrador":
            print "hola"
        else:
            us=QuinielaCuartos.objects.filter(nombreUsuario=tipo)[12:]
            if us:
                return render_to_response('error.html',context_instance=RequestContext(request))
            x2=CalendarioCuartos.objects.all()[12:]
            for z in x2:
                a=QuinielaFinal()
                a.nombreUsuario_id=tipo
                a.iden_id=z.ide
                a.equipo1_id=z.equipo1_id
                a.equipo2_id=z.equipo2_id
                a.fecha_id=z.fecha_id
                a.save()
        return HttpResponseRedirect("/quinielaUsuario1")  
    else:
        return HttpResponseRedirect("../")   
    

def mostrarQuinielas_view(request):
    if request.user.is_authenticated():
            nombre=request.user
            tipo=nombre.id
            x1=UserProfile.objects.filter(usuario=tipo)
            for x in x1:
                tipo3=x.tipoPerfil.tipo
            if tipo3 == "administrador":
                return HttpResponseRedirect('../')
            else:
                return render_to_response('rellenaQuinielas.html',context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')
    
def QuinielaForm_view(request,time):
    gol1=0
    gol2=0
    gol={}
    i=1
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "administrador":
            return HttpResponseRedirect('../')
        else:
            cal=CalendarioFase.objects.all()
            for u in cal:
                zi=u.gol1
                break
            if zi != None:
                return render_to_response('error.html',context_instance=RequestContext(request))
            if request.method=="POST":
                formulario=QuinielaForm(request.POST)
                if formulario.is_valid(): 
                    for j in range(17):
                        if j==1:
                            gol[j]=formulario.cleaned_data['gol1_1']
                        elif j==2:    
                            gol[j]=formulario.cleaned_data['gol2_1']
                        elif j==3:
                            gol[j]=formulario.cleaned_data['gol1_2']
                        elif j==4:
                            gol[j]=formulario.cleaned_data['gol2_2']
                        elif j==5:
                            gol[j]=formulario.cleaned_data['gol1_3']
                        elif j==6:    
                            gol[j]=formulario.cleaned_data['gol2_3']
                        elif j==7:
                            gol[j]=formulario.cleaned_data['gol1_4']
                        elif j==8:    
                            gol[j]=formulario.cleaned_data['gol2_4']
                        elif j==9:
                            gol[j]=formulario.cleaned_data['gol1_5']
                        elif j==10:    
                            gol[j]=formulario.cleaned_data['gol2_5']
                        elif j==11:
                            gol[j]=formulario.cleaned_data['gol1_6']
                        elif j==12:    
                            gol[j]=formulario.cleaned_data['gol2_6']
                        elif j==13:
                            gol[j]=formulario.cleaned_data['gol1_7']
                        elif j==14:    
                            gol[j]=formulario.cleaned_data['gol2_7']
                        elif j==15:
                            gol[j]=formulario.cleaned_data['gol1_8']
                        elif j==16:    
                            gol[j]=formulario.cleaned_data['gol2_8']
                    time=formulario.cleaned_data['date']
                    quini=Quiniela.objects.filter(nombreUsuario=tipo,fecha=time)
                    i=1
                    for x4 in quini:
                        x4.gol1=gol[i]
                        i=i+1
                        x4.gol2=gol[i]
                        i=i+1
                        print x4.gol1,x4.gol2
                        x4.save()
                    ctx={'tipo2':tipo2}
                    return render_to_response('rellenaQuinielas.html',ctx,context_instance=RequestContext(request)) 
                else:
                    
                    return render_to_response('error.html',context_instance=RequestContext(request))
            else:
                x2=Quiniela.objects.filter(nombreUsuario=tipo,fecha=time)
                formulario=QuinielaForm()
                ctx={'form':formulario,'x2':x2,'time':time,'tipo2':tipo2}
                return render_to_response('quiniela.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')
    
    
    
def Quiniela8Form_view(request,time):
    i=1
    l=1
    if (time):
        lista=time.split('-')
        menor=lista[0]
        mayor=lista[1]
    gol={}
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "administrador":
            return HttpResponseRedirect('../')
        else:
            cal=CalendarioOctavos.objects.all()
            for u in cal:
                zi=u.gol1
                break
            if zi:
                return render_to_response('error.html',context_instance=RequestContext(request))
            if request.method=="POST":
                formulario=QuinielaForm(request.POST)
                if formulario.is_valid(): 
                    for j in range(17):
                        if j==1:
                            gol[j]=formulario.cleaned_data['gol1_1']
                        elif j==2:    
                            gol[j]=formulario.cleaned_data['gol2_1']
                        elif j==3:
                            gol[j]=formulario.cleaned_data['gol1_2']
                        elif j==4:
                            gol[j]=formulario.cleaned_data['gol2_2']
                        elif j==5:
                            gol[j]=formulario.cleaned_data['gol1_3']
                        elif j==6:    
                            gol[j]=formulario.cleaned_data['gol2_3']
                        elif j==7:
                            gol[j]=formulario.cleaned_data['gol1_4']
                        elif j==8:    
                            gol[j]=formulario.cleaned_data['gol2_4']
                        elif j==9:
                            gol[j]=formulario.cleaned_data['gol1_5']
                        elif j==10:    
                            gol[j]=formulario.cleaned_data['gol2_5']
                        elif j==11:
                            gol[j]=formulario.cleaned_data['gol1_6']
                        elif j==12:    
                            gol[j]=formulario.cleaned_data['gol2_6']
                        elif j==13:
                            gol[j]=formulario.cleaned_data['gol1_7']
                        elif j==14:    
                            gol[j]=formulario.cleaned_data['gol2_7']
                        elif j==15:
                            gol[j]=formulario.cleaned_data['gol1_8']
                        elif j==16:    
                            gol[j]=formulario.cleaned_data['gol2_8']
                    time=formulario.cleaned_data['date']
                    lista=time.split('-')
                    menor=lista[0]
                    mayor=lista[1]
                    quini=QuinielaOctavos.objects.filter(nombreUsuario=tipo)[menor:mayor]
                    i=1
                    for x4 in quini:
                        x4.gol1=gol[i]
                        i=i+1
                        x4.gol2=gol[i]
                        i=i+1
                        print x4.gol1,x4.gol2
                        x4.save()
                    ctx={'tipo2':tipo2}
                    return render_to_response('rellenaQuinielasOctavos.html',ctx,context_instance=RequestContext(request))
                else:      
                    return render_to_response('error.html',context_instance=RequestContext(request))
            else:
                x2=QuinielaOctavos.objects.filter(nombreUsuario=tipo)[menor:mayor]
                formulario=QuinielaForm()
                ctx={'form':formulario,'x2':x2,'time':time,'tipo2':tipo2}
                return render_to_response('quiniela8.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')
    
    
def Quiniela4Form_view(request):
    i=1
    gol={}
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "administrador":
            return HttpResponseRedirect('../')
        else:
            cal=CalendarioCuartos.objects.all()
            for u in cal:
                zi=u.gol1
                break
            if zi != None:
                return render_to_response('error.html',context_instance=RequestContext(request))
            if request.method=="POST":
                formulario=QuinielaForm4(request.POST)
                if formulario.is_valid(): 
                    for j in range(17):
                        if j==1:
                            gol[j]=formulario.cleaned_data['gol1_1']
                        elif j==2:    
                            gol[j]=formulario.cleaned_data['gol2_1']
                        elif j==3:
                            gol[j]=formulario.cleaned_data['gol1_2']
                        elif j==4:
                            gol[j]=formulario.cleaned_data['gol2_2']
                        elif j==5:
                            gol[j]=formulario.cleaned_data['gol1_3']
                        elif j==6:    
                            gol[j]=formulario.cleaned_data['gol2_3']
                        elif j==7:
                            gol[j]=formulario.cleaned_data['gol1_4']
                        elif j==8:    
                            gol[j]=formulario.cleaned_data['gol2_4']
                        elif j==9:
                            gol[j]=formulario.cleaned_data['gol1_5']
                        elif j==10:    
                            gol[j]=formulario.cleaned_data['gol2_5']
                        elif j==11:
                            gol[j]=formulario.cleaned_data['gol1_6']
                        elif j==12:    
                            gol[j]=formulario.cleaned_data['gol2_6']
                        elif j==13:
                            gol[j]=formulario.cleaned_data['gol1_7']
                        elif j==14:    
                            gol[j]=formulario.cleaned_data['gol2_7']
                        elif j==15:
                            gol[j]=formulario.cleaned_data['gol1_8']
                        elif j==16:    
                            gol[j]=formulario.cleaned_data['gol2_8']
                    
                    
                    quini=QuinielaCuartos.objects.filter(nombreUsuario=tipo)
                    i=1
                    for x4 in quini:
                        x4.gol1=gol[i]
                        i=i+1
                        x4.gol2=gol[i]
                        i=i+1
                        print x4.gol1,x4.gol2
                        x4.save()
                    return HttpResponseRedirect('../')
                else:
                    
                    return render_to_response('error.html',context_instance=RequestContext(request))
            else:
                x2=QuinielaCuartos.objects.filter(nombreUsuario=tipo)
                formulario=QuinielaForm4()
                ctx={'form':formulario,'x2':x2,'tipo2':tipo2}
                return render_to_response('quiniela4.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')

def Quiniela2Form_view(request):
    i=1
    gol={}
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo
            tipo3=x.tipoPerfil.tipo
        if tipo3 == "administrador":
            return HttpResponseRedirect('../')
        else:
            cal=CalendarioCuartos.objects.all()[8:]
            for u in cal:
                zi=u.gol1
                break
            if zi:
                return render_to_response('error.html',context_instance=RequestContext(request))
            
            if request.method=="POST":
                formulario=Quiniela2Form(request.POST)
                if formulario.is_valid(): 
                    for j in range(9):
                        if j==1:
                            gol[j]=formulario.cleaned_data['gol1_1']
                        elif j==2:    
                            gol[j]=formulario.cleaned_data['gol2_1']
                        elif j==3:
                            gol[j]=formulario.cleaned_data['gol1_2']
                        elif j==4:
                            gol[j]=formulario.cleaned_data['gol2_2']
                        elif j==5:
                            gol[j]=formulario.cleaned_data['gol1_3']
                        elif j==6:    
                            gol[j]=formulario.cleaned_data['gol2_3']
                        elif j==7:
                            gol[j]=formulario.cleaned_data['gol1_4']
                        elif j==8:    
                            gol[j]=formulario.cleaned_data['gol2_4']
                    
                    quini=QuinielaSemi.objects.filter(nombreUsuario=tipo)
                    i=1
                    for x4 in quini:
                        x4.gol1=gol[i]
                        i=i+1
                        x4.gol2=gol[i]
                        i=i+1
                        print x4.gol1,x4.gol2
                        x4.save()
                    return HttpResponseRedirect('../')
                else:
                    
                    return render_to_response('error.html',context_instance=RequestContext(request))
            else:
                x2=QuinielaSemi.objects.filter(nombreUsuario=tipo)
                formulario=Quiniela2Form()
                ctx={'form':formulario,'x2':x2,'tipo2':tipo2}
                return render_to_response('quiniela.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')
        
def Quiniela1Form_view(request):
    i=1
    gol={}
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo3=x.tipoPerfil.tipo
            tipo2=x.tipoPerfil.tipo
        if tipo3 == "administrador":
            return HttpResponseRedirect('../')
        else:
            cal=CalendarioCuartos.objects.all()[12:]
            for u in cal:
                zi=u.gol1
                break
            if zi:
                return render_to_response('error.html',context_instance=RequestContext(request))
            
            if request.method=="POST":
                formulario=Quiniela1Form(request.POST)
                if formulario.is_valid(): 
                    for j in range(9):
                        if j==1:
                            gol[j]=formulario.cleaned_data['gol1_1']
                        elif j==2:    
                            gol[j]=formulario.cleaned_data['gol2_1']
                    quini=QuinielaFinal.objects.filter(nombreUsuario=tipo)
                    i=1
                    for x4 in quini:
                        x4.gol1=gol[i]
                        i=i+1
                        x4.gol2=gol[i]
                        i=i+1
                        print x4.gol1,x4.gol2
                        x4.save()
                    return HttpResponseRedirect('../')
                else:
                    
                    return render_to_response('error.html',context_instance=RequestContext(request))
            else:
                x2=QuinielaFinal.objects.filter(nombreUsuario=tipo)
                formulario=Quiniela1Form()
                ctx={'form':formulario,'x2':x2,'tipo2':tipo2}
                return render_to_response('quiniela.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')
        
def menuForm_view(request):
    veri=Verificacion.objects.filter(registro=3)
    regi=0
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
                tipo2=x.tipoPerfil.tipo
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
                                                    fase1="NO"
                                                    break
                                            break
                                    break
                            break
                    break
            
            quiniF=Quiniela.objects.filter(nombreUsuario=tipo)
            quini8=QuinielaOctavos.objects.filter(nombreUsuario=tipo)
            quini4=QuinielaCuartos.objects.filter(nombreUsuario=tipo)
            quini2=QuinielaSemi.objects.filter(nombreUsuario=tipo)
            quini1=QuinielaFinal.objects.filter(nombreUsuario=tipo)
            ctx={'tipo2':tipo2,'tipo':tipo3,'fase1':fase1,'fase2':fase2,'fase4':fase4,'fase8':fase8,'faseG':faseG,'x1':x1,'quiniF':quiniF,'quini8':quini8,'quini4':quini4,'quini2':quini2,'quini1':quini1}
            return render_to_response('menu.html',ctx,context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('../')  
    else:
        return HttpResponseRedirect('../')
    
    
def mostrarQuinielaF_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo    
        quiniF=Quiniela.objects.filter(nombreUsuario=tipo)
        fase="grupo"                
        eq=CalendarioFase.objects.all()
        for y in eq:
            cal=y.gol1
            break
        ctx={'quiniF':quiniF,'cal':cal,'fase':fase,'tipo2':tipo2}
        return render_to_response('vistaQuiniela1.html',ctx,context_instance=RequestContext(request))


def mostrarQuiniela8_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo    
        fase="8"    
        quiniF=QuinielaOctavos.objects.filter(nombreUsuario=tipo)
        eq=CalendarioOctavos.objects.all()
        for y in eq:
            cal=y.gol1
            break
        ctx={'quiniF':quiniF,'cal':cal,'fase':fase,'tipo2':tipo2}
        return render_to_response('vistaQuiniela1.html',ctx,context_instance=RequestContext(request))

def mostrarQuiniela4_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id    
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo  
        fase="4"
        quiniF=QuinielaCuartos.objects.filter(nombreUsuario=tipo)
        eq=CalendarioCuartos.objects.all()[:8]
        for y in eq:
            cal=y.gol1
            break
        ctx={'quiniF':quiniF,'cal':cal,'fase':fase,'tipo2':tipo2}
        return render_to_response('vistaQuiniela1.html',ctx,context_instance=RequestContext(request))

def mostrarQuiniela2_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo      
        quiniF=QuinielaSemi.objects.filter(nombreUsuario=tipo)
        eq=CalendarioCuartos.objects.all()[8:12]
        fase="2"
        for y in eq:
            cal=y.gol1
            break
        ctx={'quiniF':quiniF,'cal':cal,'fase':fase,'tipo2':tipo2}
        return render_to_response('vistaQuiniela1.html',ctx,context_instance=RequestContext(request))

def mostrarQuiniela1_view(request):
    if request.user.is_authenticated():
        nombre=request.user
        tipo=nombre.id    
        x1=UserProfile.objects.filter(usuario=tipo)
        for x in x1:
            tipo2=x.tipoPerfil.tipo  
        quiniF=QuinielaFinal.objects.filter(nombreUsuario=tipo)
        eq=CalendarioCuartos.objects.all()[12:]
        fase="1"
        for y in eq:
            cal=y.gol1
        ctx={'quiniF':quiniF,'cal':cal,'fase':fase,'tipo2':tipo2}
        return render_to_response('vistaQuiniela1.html',ctx,context_instance=RequestContext(request))

def mostrarQuinielasOctavos_view(request):
    if request.user.is_authenticated():
            nombre=request.user
            tipo=nombre.id
            x1=UserProfile.objects.filter(usuario=tipo)
            for x in x1:
                tipo3=x.tipoPerfil.tipo
                tipo2=x.tipoPerfil.tipo
            if tipo3 == "administrador":
                return HttpResponseRedirect('../')
            else:
                ctx={'tipo2':tipo2}
                return render_to_response('rellenaQuinielasOctavos.html',ctx,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('../')
    
    
def modificarQuinielas_view(request,l):
    fase=""
    ctx={}
    q=""
    e=""
    if request.user.is_authenticated():
            nombre=request.user
            tipo=nombre.id
            x1=UserProfile.objects.filter(usuario=tipo)
            for x in x1:
                tipo3=x.tipoPerfil.tipo
                tipo2=x.tipoPerfil.tipo
            if tipo3 == "administrador":
                return HttpResponseRedirect('../')
            else:
                if request.method=='POST':
                    form=modificarForm(request.POST)
                    if form.is_valid():
                        gol1=request.POST['gol1']
                        gol2=request.POST['gol2']
                        fase=request.POST['fase']
                        equipo1F=request.POST['equipo1']
                        equipo2F=request.POST['equipo2'] 
                        if fase=="grupo":
                            q=Quiniela.objects.filter(equipo1=equipo1F,equipo2=equipo2F,nombreUsuario=tipo)
                            for u in q:
                                u.gol1=gol1
                                u.gol2=gol2
                                u.save()
                        elif fase=="8":
                            q=QuinielaOctavos.objects.filter(equipo1=equipo1F,equipo2=equipo2F,nombreUsuario=tipo)
                            for u in q:
                                u.gol1=gol1
                                u.gol2=gol2
                                u.save()
                        elif fase=="4":
                            q=QuinielaCuartos.objects.filter(equipo1=equipo1F,equipo2=equipo2F,nombreUsuario=tipo)
                            for u in q:
                                u.gol1=gol1
                                u.gol2=gol2
                                u.save()
                        elif fase=="2":
                            q=QuinielaSemi.objects.filter(equipo1=equipo1F,equipo2=equipo2F,nombreUsuario=tipo)
                            for u in q:
                                u.gol1=gol1
                                u.gol2=gol2
                                u.save()
                        elif fase=="1":   
                            q=QuinielaFinal.objects.filter(equipo1=equipo1F,equipo2=equipo2F,nombreUsuario=tipo)
                            for u in q:
                                u.gol1=gol1
                                u.gol2=gol2
                                u.save() 
                        mensaje1="Sus cambios han sido guardados exitosamente"
                        ctx={'mensaje1':mensaje1,'tipo2':tipo2}    
                        return render_to_response('index.html',ctx,context_instance=RequestContext(request))
                    else:
                        return HttpResponseRedirect("../")
                else: 
                    if (l):
                        lista=l.split('-')
                        f=lista[0]
                        equip1=lista[1]
                        equip2=lista[2]
                        form=modificarForm()
                        if f=="grupo":
                            e=Quiniela.objects.filter(equipo1=equip1,equipo2=equip2,nombreUsuario=tipo)
                        elif f=="8":
                            e=QuinielaOctavos.objects.filter(equipo1=equip1,equipo2=equip2,nombreUsuario=tipo)
                        elif f=="4":
                            e=QuinielaCuartos.objects.filter(equipo1=equip1,equipo2=equip2,nombreUsuario=tipo)
                        elif f=="2":
                            e=QuinielaSemi.objects.filter(equipo1=equip1,equipo2=equip2,nombreUsuario=tipo)
                        elif f=="1":   
                            e=QuinielaFinal.objects.filter(equipo1=equip1,equipo2=equip2,nombreUsuario=tipo)
                        ctx={'form':form,'e':e,'f':f,'tipo2':tipo2}
                        return render_to_response('modificar.html',ctx,context_instance=RequestContext(request))
                    else:
                        return HttpResponseRedirect("../")
    else:
        return HttpResponseRedirect("../")
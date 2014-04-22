from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from quiniela.apps.champions.aletorio import aleatorio
from quiniela.apps.champions.puntos import Puntos
from quiniela.apps.champions.models import Equipos, CalendarioFase,CalendarioOctavos,CalendarioCuartos, FaseDeGrupos, Grupos
import random



def simular_view(request):   
    equipo=CalendarioFase.objects.all()
    for x in equipo:
        e1=x.equipo1_id
        e2=x.equipo2_id
        nivel1=Equipos.objects.filter(club=e1)
        nivel2=Equipos.objects.filter(club=e2) 
        for q in nivel1:
                m1=q.nivel.level 
        for z in nivel2:
                n1=z.nivel.level
        m=int(m1)
        n=int(n1)
        a=aleatorio(1,5)
        a1=a.obtener()*0.20
        if a1>0.20:
            if m==n:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()        
                    x.gol1=f1
                    x.gol2=g1
        
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
            if m==1 and n ==2:
               
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
              
            if m==1 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,4)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
         
                else:
                    f=aleatorio(1,4)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
           
            if m==1 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,5)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    x.save()
                else:
                    f=aleatorio(1,5)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
               
            if m==2 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
              
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                
            if m==2 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                  
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
            if m==2 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
               
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                   
            if m==3 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,4)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                  
                else:
                    f=aleatorio(1,4)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                  
            if m==3 and n ==2:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                
            if m==3 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                   
            if m==4 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,5)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,5)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
            if m==4 and n ==2:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
            if m==4 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
        else:
            h=aleatorio(1,3)
            h1=h.obtener()
            f1=h1
            g1=h1
            x.gol1=f1
            x.gol2=g1
             
        x.save()
        puto=Puntos(e1,e2,f1,g1)
        puto.colocar()
    return HttpResponseRedirect("/octavos")  

def simular8_view(request):
    equipo=CalendarioOctavos.objects.all()
    for x in equipo:
        e1=x.equipo1_id
        e2=x.equipo2_id
        nivel1=Equipos.objects.filter(club=e1)
        nivel2=Equipos.objects.filter(club=e2) 
        for q in nivel1:
                m1=q.nivel.level 
        for z in nivel2:
                n1=z.nivel.level
        m=int(m1)
        n=int(n1)
        a=aleatorio(1,5)
        a1=a.obtener()*0.20
        if a1>0.20:
            if m==n:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()        
                    x.gol1=f1
                    x.gol2=g1
        
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
            if m==1 and n ==2:
               
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
              
            if m==1 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,4)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
         
                else:
                    f=aleatorio(1,4)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
           
            if m==1 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,5)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    x.save()
                else:
                    f=aleatorio(1,5)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
               
            if m==2 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
              
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                
            if m==2 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                  
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
            if m==2 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
               
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                   
            if m==3 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,4)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                  
                else:
                    f=aleatorio(1,4)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                  
            if m==3 and n ==2:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                
            if m==3 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                   
            if m==4 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,5)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,5)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
            if m==4 and n ==2:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
            if m==4 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
        else:
            h=aleatorio(0,3)
            h1=h.obtener()
            f1=h1
            g1=h1
            x.gol1=f1
            x.gol2=g1
             
        x.save()

    return HttpResponseRedirect("/cuartos")  


def simular4_view(request):
    equipo=CalendarioCuartos.objects.all()
    for x in equipo:
        e1=x.equipo1_id
        e2=x.equipo2_id
        nivel1=Equipos.objects.filter(club=e1)
        nivel2=Equipos.objects.filter(club=e2) 
        for q in nivel1:
                m1=q.nivel.level 
        for z in nivel2:
                n1=z.nivel.level
        m=int(m1)
        n=int(n1)
        a=aleatorio(1,5)
        a1=a.obtener()*0.20
        if a1>0.20:
            if m==n:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()        
                    x.gol1=f1
                    x.gol2=g1
        
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
            if m==1 and n ==2:
               
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
              
            if m==1 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,4)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
         
                else:
                    f=aleatorio(1,4)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
           
            if m==1 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.80
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,5)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    x.save()
                else:
                    f=aleatorio(1,5)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
               
            if m==2 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
              
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                
            if m==2 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                  
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
            if m==2 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.60
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
               
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                   
            if m==3 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,4)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                  
                else:
                    f=aleatorio(1,4)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                  
            if m==3 and n ==2:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                
            if m==3 and n ==4:
                c=aleatorio(1,5)
                c1=c.obtener()*0.40
                c2=c.obtener()*0.20
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                   
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                                   
            if m==4 and n ==1:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.80
                if c1>c2:
                    f=aleatorio(1,5)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,5)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
            if m==4 and n ==2:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.60
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
            if m==4 and n ==3:
                c=aleatorio(1,5)
                c1=c.obtener()*0.20
                c2=c.obtener()*0.40
                if c1>c2:
                    f=aleatorio(1,3)
                    f1=f.obtener()
                    f2=f1-1
                    g=aleatorio(0,f2)
                    g1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
                else:
                    f=aleatorio(1,3)
                    g1=f.obtener()
                    g2=g1-1
                    g=aleatorio(0,g2)
                    f1=g.obtener()
                    x.gol1=f1
                    x.gol2=g1
                    
        else:
            h=aleatorio(0,3)
            h1=h.obtener()
            f1=h1
            g1=h1
            x.gol1=f1
            x.gol2=g1
             
        x.save()

    return HttpResponseRedirect("/semi")

def simularsemi_view(request):
    p=5
    for i in range(2):
        print p
        equipo=CalendarioCuartos.objects.filter(juego=p)
        p=p+1
        for x in equipo:
            e1=x.equipo1_id
            e2=x.equipo2_id
            nivel1=Equipos.objects.filter(club=e1)
            nivel2=Equipos.objects.filter(club=e2) 
            for q in nivel1:
                    m1=q.nivel.level 
            for z in nivel2:
                    n1=z.nivel.level
            m=int(m1)
            n=int(n1)
            a=aleatorio(1,5)
            a1=a.obtener()*0.20
            if a1>0.20:
                if m==n:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.80
                    c2=c.obtener()*0.80
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()        
                        x.gol1=f1
                        x.gol2=g1
            
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                if m==1 and n ==2:
                   
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.80
                    c2=c.obtener()*0.60
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                  
                if m==1 and n ==3:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.80
                    c2=c.obtener()*0.40
                    if c1>c2:
                        f=aleatorio(1,4)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
             
                    else:
                        f=aleatorio(1,4)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
               
                if m==1 and n ==4:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.80
                    c2=c.obtener()*0.20
                    if c1>c2:
                        f=aleatorio(1,5)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        x.save()
                    else:
                        f=aleatorio(1,5)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                   
                if m==2 and n ==1:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.60
                    c2=c.obtener()*0.80
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                  
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                    
                if m==2 and n ==3:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.60
                    c2=c.obtener()*0.40
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                      
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                       
                if m==2 and n ==4:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.60
                    c2=c.obtener()*0.20
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                   
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                                       
                if m==3 and n ==1:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.40
                    c2=c.obtener()*0.80
                    if c1>c2:
                        f=aleatorio(1,4)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                      
                    else:
                        f=aleatorio(1,4)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                                      
                if m==3 and n ==2:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.40
                    c2=c.obtener()*0.60
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                       
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                    
                if m==3 and n ==4:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.40
                    c2=c.obtener()*0.20
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                       
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                                       
                if m==4 and n ==1:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.20
                    c2=c.obtener()*0.80
                    if c1>c2:
                        f=aleatorio(1,5)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                    else:
                        f=aleatorio(1,5)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                if m==4 and n ==2:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.20
                    c2=c.obtener()*0.60
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                    
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                if m==4 and n ==3:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.20
                    c2=c.obtener()*0.40
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
            else:
                h=aleatorio(0,3)
                h1=h.obtener()
                f1=h1
                g1=h1
                x.gol1=f1
                x.gol2=g1
                 
            x.save()

    return HttpResponseRedirect("/final")

def simularfinal_view(request):
    p=7
    for i in range(1):
        equipo=CalendarioCuartos.objects.filter(juego=p)
        for x in equipo:
            e1=x.equipo1_id
            e2=x.equipo2_id
            nivel1=Equipos.objects.filter(club=e1)
            nivel2=Equipos.objects.filter(club=e2) 
            for q in nivel1:
                    m1=q.nivel.level 
            for z in nivel2:
                    n1=z.nivel.level
            m=int(m1)
            n=int(n1)
            a=aleatorio(1,5)
            a1=a.obtener()*0.20
            if a1>0.20:
                if m==n:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.80
                    c2=c.obtener()*0.80
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()        
                        x.gol1=f1
                        x.gol2=g1
            
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                if m==1 and n ==2:
                   
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.80
                    c2=c.obtener()*0.60
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                  
                if m==1 and n ==3:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.80
                    c2=c.obtener()*0.40
                    if c1>c2:
                        f=aleatorio(1,4)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
             
                    else:
                        f=aleatorio(1,4)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
               
                if m==1 and n ==4:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.80
                    c2=c.obtener()*0.20
                    if c1>c2:
                        f=aleatorio(1,5)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        x.save()
                    else:
                        f=aleatorio(1,5)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                   
                if m==2 and n ==1:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.60
                    c2=c.obtener()*0.80
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                  
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                    
                if m==2 and n ==3:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.60
                    c2=c.obtener()*0.40
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                      
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                       
                if m==2 and n ==4:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.60
                    c2=c.obtener()*0.20
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                   
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                                       
                if m==3 and n ==1:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.40
                    c2=c.obtener()*0.80
                    if c1>c2:
                        f=aleatorio(1,4)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                      
                    else:
                        f=aleatorio(1,4)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                                      
                if m==3 and n ==2:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.40
                    c2=c.obtener()*0.60
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                       
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                    
                if m==3 and n ==4:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.40
                    c2=c.obtener()*0.20
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                       
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                                       
                if m==4 and n ==1:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.20
                    c2=c.obtener()*0.80
                    if c1>c2:
                        f=aleatorio(1,5)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                    else:
                        f=aleatorio(1,5)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                if m==4 and n ==2:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.20
                    c2=c.obtener()*0.60
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                    
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                if m==4 and n ==3:
                    c=aleatorio(1,5)
                    c1=c.obtener()*0.20
                    c2=c.obtener()*0.40
                    if c1>c2:
                        f=aleatorio(1,3)
                        f1=f.obtener()
                        f2=f1-1
                        g=aleatorio(0,f2)
                        g1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
                    else:
                        f=aleatorio(1,3)
                        g1=f.obtener()
                        g2=g1-1
                        g=aleatorio(0,g2)
                        f1=g.obtener()
                        x.gol1=f1
                        x.gol2=g1
                        
            else:
                ganador=aleatorio(1,2)
                h=aleatorio(0,3)
                ganadorF=ganador.obtener()
                h1=h.obtener()
                f1=h1
                g1=h1
                golG=6
                golP=5
                if ganadorF==1:
                    x.gol1=f1+golG
                    x.gol2=g1+golP
                    
                else:
                    x.gol2=g1+golG
                    x.gol1=f1+golP
            x.save()

    return HttpResponseRedirect("/puntaje1")


def hacerOctavos_view(request):
    i=1
    octavos={}
    calendario={}
    grupos=Grupos.objects.all()
    for x in grupos:
        equipos1=FaseDeGrupos.objects.filter(numeroGrupo=x.numeroGrupo).order_by('-puntos','-golesFavor')[:2]
        for z in equipos1:
            if i==1:
                pos=i
                pais=z.nombreClub.pais_id
                grupo=z.numeroGrupo_id
                equipo=z.nombreClub_id
                octavos[equipo]=(pais,pos,grupo)
                i=i+1
            else:
                pos=i
                pais=z.nombreClub.pais_id
                grupo=z.numeroGrupo_id
                equipo=z.nombreClub_id
                octavos[equipo]=(pais,pos,grupo)
                i=i-1
    z=0
    while z!=8:
        y=octavos.copy()
        for i in range(8):
            b=""
            c=""
            pos_1=[]
            pos_2=[]
            for k,v in octavos.iteritems():
                if v[1] ==1:
                    pos_1.append(k)
            b = random.choice(pos_1)
            for k,v in octavos.iteritems():
                if octavos[b][0]!=v[0] and octavos[b][1]!=v[1] and octavos[b][2]!=v[2]:
                    pos_2.append(k)
            if len(pos_2)==0:
                break 
            else:
                c = random.choice(pos_2)
            calendario [b]=c
            del octavos[c]
            del octavos[b]
        z=len(calendario)
        if z<8:
            octavos=y.copy()
    zor=1
    for e,r in calendario.iteritems():
        h=CalendarioOctavos()
        h.equipo1_id=e
        h.equipo2_id=r
        h.fecha_id="18-09-2012"
        h.juego=zor
        zor=zor+1
        h.save()
    zor=1
    for e,r in calendario.iteritems():
        h=CalendarioOctavos()
        h.equipo1_id=r
        h.equipo2_id=e
        h.juego=zor
        h.fecha_id="18-09-2012"
        zor=zor+1
        h.save()
    return HttpResponseRedirect("/puntaje")



def hacerCuartos_view(request):
    x=1
    cuartos={}
    equipo=[]
    empate=[]
    gol1=0
    gol2=0
    golL1=0
    golL2=0
    golV1=0
    golV2=0
    for i in range(9):
        octavos=CalendarioOctavos.objects.filter(juego=i)
        for j in octavos:
            if x==1:
                gol1=gol1+j.gol1
                gol2=gol2+j.gol2
                golL1=j.gol1
                golV1=j.gol2
                x=x+1
            else:
                golL2=j.gol1
                golV2=j.gol2
                gol2=gol2+j.gol1
                gol1=gol1+j.gol2
                x=x-1
                if gol1>gol2:
                    equipo.append(j.equipo2_id)
    
                elif gol2>gol1:
                    equipo.append(j.equipo1_id)
    
                else:
                    if golL1==golL2 and golV1==golV2:
                        empate.append(j.equipo1_id)
                        empate.append(j.equipo2_id)
                        b = random.choice(empate)
                        equipo.append(b)
                        d = empate.index(b)
                        golG=6
                        golP=5
                        if d==0:
                            j.gol1=golG+j.gol1
                            j.gol2=golP+j.gol2
                        else:
                            j.gol2=golG+j.gol2
                            j.gol1=golP+j.gol1
                        empate=[]
                        j.save()
                    else:
                        if golV1>golV2:
                            equipo.append(j.equipo1_id)
                        else:
                            equipo.append(j.equipo2_id)
                gol1=0
                gol2=0
                golL2=0
                golL1=0
                golV1=0                    
                golV2=0
    for j in range(4):
        equi1 = random.choice(equipo)
        d = equipo.index(equi1)
        del equipo [d]
        equi2 = random.choice(equipo)
        d = equipo.index(equi2)
        del equipo [d]
        cuartos [equi1]=equi2
    zor=1
    for e,r in cuartos.iteritems():
        h=CalendarioCuartos()
        h.equipo1_id=e
        h.equipo2_id=r
        h.fecha_id="18-09-2012"
        h.juego=zor
        zor=zor+1
        h.save()
    zor=1
    for e,r in cuartos.iteritems():
        h=CalendarioCuartos()
        h.equipo1_id=r
        h.equipo2_id=e
        h.juego=zor
        h.fecha_id="18-09-2012"
        zor=zor+1
        h.save()
    return HttpResponseRedirect("/puntaje8")

def hacerSemi_view(request):
    x=1
    golL1=0
    golL2=0
    golV1=0
    golV2=0
    semis={}
    equipo=[]
    empate=[]
    gol1=0
    gol2=0
    for i in range(5):
        octavos=CalendarioCuartos.objects.filter(juego=i)
        for j in octavos:
            if x==1:
                gol1=gol1+j.gol1
                gol2=gol2+j.gol2
                golL1=j.gol1
                golV1=j.gol2
                x=x+1
            else:
                golL2=j.gol1
                golV2=j.gol2
                gol2=gol2+j.gol1
                gol1=gol1+j.gol2
                x=x-1
                if gol1>gol2:
                    equipo.append(j.equipo2_id)

                elif gol2>gol1:
                    equipo.append(j.equipo1_id)

                else:
                    if golL1==golL2 and golV1==golV2:
                        empate.append(j.equipo1_id)
                        empate.append(j.equipo2_id)
                        b = random.choice(empate)
                        equipo.append(b)
                        d = empate.index(b)
                        golG=6
                        golP=5
                        if d==0:
                            j.gol1=golG+j.gol1
                            j.gol2=golP+j.gol2
                        else:
                            j.gol2=golG+j.gol2
                            j.gol1=golP+j.gol1
                        empate=[]
                        j.save()
                    else:
                        if golV1>golV2:
                            equipo.append(j.equipo1_id)
                        else:
                            equipo.append(j.equipo2_id)
                gol1=0
                gol2=0
                golL2=0
                golL1=0
                golV1=0                    
                golV2=0
    for j in range(2):
        if j==1:
            equi1 = equipo[0]
            equi2 = equipo[1]
            semis [equi1]=equi2
        else:
            equi1 = equipo[2]
            equi2 = equipo[3]
            semis [equi1]=equi2

    zor=5
    for e,r in semis.iteritems():
        h=CalendarioCuartos()
        h.equipo1_id=e
        h.equipo2_id=r
        h.fecha_id="04-04-2013"
        h.juego=zor
        zor=zor+1
        h.save()
    zor=5
    for e,r in semis.iteritems():
        h=CalendarioCuartos()
        h.equipo1_id=r
        h.equipo2_id=e
        h.juego=zor
        h.fecha_id="04-04-2013"
        zor=zor+1
        h.save()
    return HttpResponseRedirect("/puntaje4")
    

    

def hacerFinal_view(request):
    x=1
    p=5
    golL1=0
    golL2=0
    golV1=0
    golV2=0
    final={}
    equipo=[]
    empate=[]
    gol1=0
    gol2=0
    for i in range(3):
        octavos=CalendarioCuartos.objects.filter(juego=p)
        p=p+1
        for j in octavos:
            if x==1:
                gol1=gol1+j.gol1
                gol2=gol2+j.gol2
                golL1=j.gol1
                golV1=j.gol2
                x=x+1
            else:
                golL2=j.gol1
                golV2=j.gol2
                gol2=gol2+j.gol1
                gol1=gol1+j.gol2
                x=x-1

                if gol1>gol2:
                    equipo.append(j.equipo2_id)
                elif gol2>gol1:
                    equipo.append(j.equipo1_id)

                else:
                    if golL1==golL2 and golV1==golV2:
                        empate.append(j.equipo1_id)
                        empate.append(j.equipo2_id)
                        b = random.choice(empate)
                        equipo.append(b)
                        d = empate.index(b)
                        golG=6
                        golP=5
                        if d==0:
                            j.gol1=golG+j.gol1
                            j.gol2=golP+j.gol2
                        else:
                            j.gol2=golG+j.gol2
                            j.gol1=golP+j.gol1
                        empate=[]
                        j.save()
                    else:
                        if golV1>golV2:
                            equipo.append(j.equipo1_id)
                        else :
                            equipo.append(j.equipo2_id)
                gol1=0
                gol2=0
                golL2=0
                golL1=0
                golV1=0                    
                golV2=0
    equi1 = equipo[0]
    equi2 = equipo[1]
    final [equi1]=equi2
    zor=7
    for e,r in final.iteritems():
        h=CalendarioCuartos()
        h.equipo1_id=e
        h.equipo2_id=r
        h.fecha_id="21-04-2013"
        h.juego=zor
        h.save()

    return HttpResponseRedirect("/puntaje2")


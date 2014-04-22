from quiniela.apps.champions.models import FaseDeGrupos

class Puntos: 
    local=""
    visitante=""
    golesL=""
    golesV=""

    def __init__(self,e1,e2,g1,g2):
        self.golesL=g1
        self.golesV=g2
        self.local=e1
        self.visitante=e2
    
    def colocar(self):
        if self.golesL>self.golesV:
            faseG=FaseDeGrupos.objects.filter(nombreClub=self.local)
            for q1 in faseG:
                jugados=q1.juegosJugados
                q1.juegosJugados=jugados+1
                golF=q1.golesFavor
                golC=q1.golesContra
                punto=q1.puntos
                q1.golesFavor=self.golesL+golF
                q1.golesContra=self.golesV+golC
                q1.puntos=3+punto
                ganados=q1.juegosGanados
                q1.juegosGanados=ganados+1
                
                q1.save()
            faseG2=FaseDeGrupos.objects.filter(nombreClub=self.visitante)
            for w1 in faseG2:
                golF=w1.golesFavor
                golC=w1.golesContra
                jugados=w1.juegosJugados
                w1.juegosJugados=jugados+1
                w1.golesFavor=self.golesV+golF
                w1.golesContra=self.golesL+golC
                
                perdidos=w1.juegosPerdidos
                w1.juegosPerdidos=perdidos+1
                
                w1.save()
        elif self.golesL<self.golesV:
            faseG2=FaseDeGrupos.objects.filter(nombreClub=self.visitante)
            for q2 in faseG2:
                golF=q2.golesFavor
                golC=q2.golesContra
                punto=q2.puntos
                jugados=q2.juegosJugados
                q2.juegosJugados=jugados+1
                q2.golesFavor=self.golesV+golF
                q2.golesContra=self.golesL+golC
                q2.puntos=3+punto
                ganados=q2.juegosGanados
                q2.juegosGanados=ganados+1
                q2.save()
            faseG=FaseDeGrupos.objects.filter(nombreClub=self.local)
            for w2 in faseG:
                golF=w2.golesFavor
                golC=w2.golesContra
                jugados=w2.juegosJugados
                w2.juegosJugados=jugados+1
                w2.golesFavor=self.golesL+golF
                w2.golesContra=self.golesV+golC
                perdidos=w2.juegosPerdidos
                w2.juegosPerdidos=perdidos+1
                w2.save()
        else:
            faseG=FaseDeGrupos.objects.filter(nombreClub=self.local)
            for q3 in faseG:
                golF=q3.golesFavor
                golC=q3.golesContra
                punto=q3.puntos
                jugados=q3.juegosJugados
                q3.juegosJugados=jugados+1
                q3.golesFavor=self.golesL+golF
                q3.golesContra=self.golesV+golC
                q3.puntos=1+punto
                
                empatados=q3.juegosEmpatados
                q3.juegosEmpatados=empatados+1
                q3.save()
            faseG2=FaseDeGrupos.objects.filter(nombreClub=self.visitante)
            for w3 in faseG2:
                golF=w3.golesFavor
                golC=w3.golesContra
                punto=w3.puntos
                jugados=w3.juegosJugados
                w3.juegosJugados=jugados+1
                w3.golesFavor=self.golesV+golF
                w3.golesContra=self.golesL+golC
                w3.puntos=1+punto
                empatados=w3.juegosEmpatados
                w3.juegosEmpatados=empatados+1
                w3.save()
        
            
            
                    
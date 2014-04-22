# enconding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Grupos(models.Model):
    numeroGrupo=models.CharField(max_length=10,primary_key=True)
    def __unicode__(self):
        numero=str(self.numeroGrupo)
        return numero

class Paises(models.Model):
    nacionalidad=models.CharField(max_length=20,primary_key=True)
    def __unicode__(self):
        return self.nacionalidad
    
class Fechas(models.Model):
    date=models.CharField(max_length=20,primary_key=True)
    def __unicode__(self):
        dia=str(self.date)
        return dia
    
class Niveles(models.Model):
    level=models.PositiveIntegerField(primary_key=True)
    def __unicode__(self):
        nivel=str(self.level)
        return nivel
        
class Equipos(models.Model):
    
    def url(self,filename):
        ruta="MultimediaData/Equipos/%s/%s"%(self.club,str(filename))
        return ruta
    
    
    club=models.CharField(max_length=20,primary_key=True)
    imagen=models.ImageField(upload_to=url,null=True,blank=True)
    pais=models.ForeignKey(Paises)
    grupo=models.ForeignKey(Grupos)
    nivel=models.ForeignKey(Niveles)
    def __unicode__(self):
        return self.club
    
    
class FaseDeGrupos(models.Model):
    nombreClub=models.ForeignKey(Equipos,unique=True)
    numeroGrupo=models.ForeignKey(Grupos)
    juegosJugados=models.PositiveIntegerField(default=0)
    juegosPerdidos=models.PositiveIntegerField(default=0)
    juegosGanados=models.PositiveIntegerField(default=0)
    juegosEmpatados=models.PositiveIntegerField(default=0)
    golesFavor=models.PositiveIntegerField(default=0)
    golesContra=models.PositiveIntegerField(default=0)
    puntos=models.PositiveIntegerField(default=0)
    def __unicode__(self):
        nombre=str(self.nombreClub)
        return nombre

class CalendarioFase(models.Model):
    ide=models.AutoField(primary_key=True)
    equipo1=models.ForeignKey(Equipos)
    equipo2=models.ForeignKey(Equipos,related_name="equipitos")
    fecha=models.ForeignKey(Fechas)
    gol1=models.IntegerField(null=True,blank=True)
    gol2=models.IntegerField(null=True,blank=True)
    def __unicode__(self):
        dia=str(self.ide)+" "+str(self.fecha)
        return dia


class CalendarioOctavos(models.Model):
    ide=models.AutoField(primary_key=True)
    juego=models.IntegerField()
    equipo1=models.ForeignKey(Equipos)
    equipo2=models.ForeignKey(Equipos,related_name="equipito")
    fecha=models.ForeignKey(Fechas)
    gol1=models.IntegerField(null=True,blank=True)
    gol2=models.IntegerField(null=True,blank=True)
    def __unicode__(self):
        dia=str(self.ide)+" "+str(self.fecha)
        return dia

    
class Quiniela(models.Model):
    iden=models.ForeignKey(CalendarioFase)
    equipo1=models.ForeignKey(Equipos)
    equipo2=models.ForeignKey(Equipos,related_name="equipo4")
    fecha=models.ForeignKey(Fechas)
    gol1=models.PositiveIntegerField(null=True,blank=True)
    gol2=models.PositiveIntegerField(null=True,blank=True)
    nombreUsuario=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombreUsuario

class QuinielaOctavos(models.Model):
    iden=models.ForeignKey(CalendarioFase)
    equipo1=models.ForeignKey(Equipos)
    equipo2=models.ForeignKey(Equipos,related_name="equipo5")
    fecha=models.ForeignKey(Fechas)
    gol1=models.PositiveIntegerField(null=True,blank=True)
    gol2=models.PositiveIntegerField(null=True,blank=True)
    nombreUsuario=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombreUsuario
    
class QuinielaCuartos(models.Model):
    iden=models.ForeignKey(CalendarioFase)
    equipo1=models.ForeignKey(Equipos)
    equipo2=models.ForeignKey(Equipos,related_name="equipo6")
    fecha=models.ForeignKey(Fechas)
    gol1=models.PositiveIntegerField(null=True,blank=True)
    gol2=models.PositiveIntegerField(null=True,blank=True)
    nombreUsuario=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombreUsuario  
    
class QuinielaSemi(models.Model):
    iden=models.ForeignKey(CalendarioFase)
    equipo1=models.ForeignKey(Equipos)
    equipo2=models.ForeignKey(Equipos,related_name="equipo7")
    fecha=models.ForeignKey(Fechas)
    gol1=models.PositiveIntegerField(null=True,blank=True)
    gol2=models.PositiveIntegerField(null=True,blank=True)
    nombreUsuario=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombreUsuario   
    
class QuinielaFinal(models.Model):
    iden=models.ForeignKey(CalendarioFase)
    equipo1=models.ForeignKey(Equipos)
    equipo2=models.ForeignKey(Equipos,related_name="equipo8")
    fecha=models.ForeignKey(Fechas)
    gol1=models.PositiveIntegerField(null=True,blank=True)
    gol2=models.PositiveIntegerField(null=True,blank=True)
    nombreUsuario=models.ForeignKey(User)
    def __unicode__(self):
        return self.nombreUsuario


        
    
class Perfiles(models.Model):
    tipo=models.CharField(max_length=20,primary_key=True)
    def __unicode__(self):
        return self.tipo

class UserProfile(models.Model):
    puntos=models.IntegerField(default=0)
    usuario=models.ForeignKey(User,unique=True)
    tipoPerfil=models.ForeignKey(Perfiles)
    nombre=models.CharField(max_length=30,unique=True)
    def __unicode__(self):
        user=str(self.usuario)
        return user


class CalendarioCuartos(models.Model):
    ide=models.AutoField(primary_key=True)
    juego=models.IntegerField()
    equipo1=models.ForeignKey(Equipos)
    equipo2=models.ForeignKey(Equipos,related_name="equipitosss")
    fecha=models.ForeignKey(Fechas)
    gol1=models.IntegerField(null=True,blank=True)
    gol2=models.IntegerField(null=True,blank=True)
    def __unicode__(self):
        dia=str(self.ide)+" "+str(self.fecha)
        return dia

class Verificacion(models.Model):
    registro=models.IntegerField()
    def __unicode__(self):
        registro=str(self.registro)
        return registro
    

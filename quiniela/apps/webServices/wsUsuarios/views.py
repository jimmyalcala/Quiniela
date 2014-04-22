from django.core import serializers
from django.http import HttpResponse
from quiniela.apps.champions.models import UserProfile 
def Usuarios_view(request):
    data=serializers.serialize("json",UserProfile.objects.filter(tipoPerfil="jugador").order_by('-puntos')[:10])
    return HttpResponse(data,mimetype="application/json")

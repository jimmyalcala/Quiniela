from django.conf.urls.defaults import patterns,url

urlpatterns=patterns('quiniela.apps.webServices.wsUsuarios.views',
                     url(r'ws/usuarios/$','Usuarios_view',name="ws_usuarios_url"),
                     )
from django.conf.urls.defaults import patterns,url

urlpatterns=patterns('quiniela.apps.Usuarios.views',
                       
                    url(r'^usuarios/$','usuarios_view',name='vista_usuarios'),
                    url(r'^crear/$','crearUsuario_view',name='vista_crear'),
                    url(r'^crearAdmin/$','crearUsuarioAdmin_view',name='vista_crearAdmin'),
                    url(r'^ingresar/$','ingresar_view',name='vista_login'),
                    url(r'^cerrar/$','logout_view',name='vista_logout'),


                       )
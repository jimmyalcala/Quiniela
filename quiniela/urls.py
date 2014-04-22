from django.conf.urls import patterns, include, url
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:}
	url(r'^',include('quiniela.apps.champions.urls')),
    url(r'^',include('quiniela.apps.simulaciones.urls')),
    url(r'^',include('quiniela.apps.calendarioQuiniela.urls')),
    url(r'^',include('quiniela.apps.Usuarios.urls')),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^',include('quiniela.apps.webServices.wsUsuarios.urls')),
    # url(r'^$', 'quiniela.views.home', name='home'),
    # url(r'^quiniela/', include('quiniela.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)

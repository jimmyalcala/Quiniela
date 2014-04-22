from django.conf.urls.defaults import patterns,url

urlpatterns=patterns('quiniela.apps.calendarioQuiniela.views',
                       
                       url(r'^mostrarQuinielas/$','mostrarQuinielas_view',name='vista_mostrarQuinielas'),
                       url(r'^quinielaUsuario/(?P<time>.*)$','QuinielaForm_view',name='vista_quiniela'),
                       url(r'^quinielaUsuario8/(?P<time>.*)$','Quiniela8Form_view',name='vista_quiniela8'),
                       url(r'^quiniela/$','hacerQuiniela_view',name='vista_hacerquiniela'),
                       url(r'^quiniela8/$','hacerQuiniela8_view',name='vista_hacerquiniela8'),
                       url(r'^quiniela4/$','hacerQuiniela4_view',name='vista_hacerquiniela4'),
                       url(r'^quiniela2/$','hacerQuiniela2_view',name='vista_hacerquiniela2'),
                       url(r'^quiniela1/$','hacerQuiniela1_view',name='vista_hacerquiniela1'),
                       url(r'^quinielaUsuario4/$','Quiniela4Form_view',name='vista_quiniela4'),
                       url(r'^quinielaUsuario2/$','Quiniela2Form_view',name='vista_quiniela2'),
                       url(r'^quinielaUsuario1/$','Quiniela1Form_view',name='vista_quiniela1'),
                       url(r'^menu/$','menuForm_view',name='vista_menu'),
                       url(r'^vistaQuinielaF/$','mostrarQuinielaF_view',name='vista_mostrarQuinielaF'),
                       url(r'^vistaQuiniela8/$','mostrarQuiniela8_view',name='vista_mostrarQuiniela8'),
                       url(r'^vistaQuiniela4/$','mostrarQuiniela4_view',name='vista_mostrarQuiniela4'),
                       url(r'^vistaQuiniela2/$','mostrarQuiniela2_view',name='vista_mostrarQuiniela2'),
                       url(r'^vistaQuiniela1/$','mostrarQuiniela1_view',name='vista_mostrarQuiniela1'),
                       url(r'^vistamostrarQuinielasOctavos/$','mostrarQuinielasOctavos_view',name='vista_mostrarQuinielaOctavos'),
                       url(r'^modificarQuinielas/(?P<l>.*)$','modificarQuinielas_view',name='vista_modificarQuinielas'),
                       
                       )
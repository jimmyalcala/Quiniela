from django.conf.urls.defaults import patterns,url

urlpatterns=patterns('quiniela.apps.simulaciones.views',
                       
                       url(r'^simular/$','simular_view',name='vista_simular'),
                       url(r'^simular8/$','simular8_view',name='vista_simular8'),
                       url(r'^simular4/$','simular4_view',name='vista_simular4'),
                       url(r'^simularsemi/$','simularsemi_view',name='vista_simularsemi'),
                       url(r'^simularfinal/$','simularfinal_view',name='vista_simularfinal'),
                       url(r'^octavos/$','hacerOctavos_view',name='vista_haceroctavos'),
                       url(r'^cuartos/$','hacerCuartos_view',name='vista_hacercuartos'),
                       url(r'^semi/$','hacerSemi_view',name='vista_hacerSemi'),
                       url(r'^final/$','hacerFinal_view',name='vista_hacerFinal'),
                       )
from django.conf.urls import patterns, url

from academico import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'materias$', views.listado_materias, name='listado_materias'),
    url(r'materia/(?P<id>\d+)$', views.materia, name='materia'),
    url(r'paralelos$', views.listado_paralelos, name='listado_paralelos'),
    url(r'buscador/paralelos/(?P<id>\d+)$', views.paralelo_buscador, name='paralelo_buscador'),
    url(r'funcion_ajax_buscador/$', views.funcion_ajax_buscador, name='funcion_ajax_buscador'),
    url(r'paralelos/periodo$', views.paralelos_periodo, name='paralelos_periodo'),
    # url(r'buscador_2$', views.buscador_placas_dos, name='buscador_placas_dos'),
    # url(r'buscador$', views.buscador_placas, name='buscador_placas'),
    # url(r'buscador_2$', views.buscador_placas_dos, name='buscador_placas_dos'),
    # url(r'funcion_ajax/$', views.funcion_ajax, name='funcion_ajax'),
    # url(r'funcion_ajax_dos/$', views.funcion_ajax_dos, name='funcion_ajax_dos'),
    # url(r'provincia/(?P<id>\d+)/mivista/aplicacion$', views.provincia, name='provincia'),
)

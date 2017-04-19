from django.conf.urls import url
from . import views

app_name = 'ejc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inscricao/$', views.InscricaoList, name='inscricao'),
    url(r'^inscricao/(?P<pk>[0-9]+)/$', views.InscricaoEdit, name='inscricao_edit'),
    url(r'^equipe/$', views.ServoList, name='servo'),
    url(r'^equipe/(?P<pk>[0-9]+)/$', views.ServoEdit, name='servo_edit'),
    url(r'^equipe/new/$', views.ServoNew, name='servo_new'),
    url(r'^secretaria/$', views.EquipesList, name='equipes'),
    url(r'^secretaria/(?P<pk>[0-9]+)/$', views.EquipesEdit, name='equipes_edit'),
    url(r'^secretaria/new/(?P<pk>[0-9]+)/$', views.EquipesNew, name='equipes_new'),
]
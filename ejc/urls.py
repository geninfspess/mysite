from django.conf.urls import url
from . import views

app_name = 'ejc'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^inscricao/$', views.InscricaoList, name='inscricao'),
    url(r'^inscricao/(?P<pk>[0-9]+)/$', views.InscricaoEdit, name='inscricao_edit'),
]
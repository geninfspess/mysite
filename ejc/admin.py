from django.contrib import admin

from .models import Inscricao
from .models import Comunidade

admin.site.register(Inscricao)
admin.site.register(Comunidade)
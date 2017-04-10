from django.contrib import admin

from .models import Inscricao
from .models import Comunidade
from .models import Encontro
from .models import Equipe
from .models import Servo
from .models import Coordenador

admin.site.register(Inscricao)
admin.site.register(Comunidade)
admin.site.register(Encontro)
admin.site.register(Equipe)
admin.site.register(Servo)
admin.site.register(Coordenador)
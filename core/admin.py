from django.contrib import admin
from .models import Materia
from .models import Assunto
from .models import Aula
from .models import Quiz

# Register your models here.
admin.site.register(Materia)
admin.site.register(Assunto)
admin.site.register(Aula)
admin.site.register(Quiz)
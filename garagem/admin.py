from django.contrib import admin

from .models import Marca
from .models import Categoria

admin.site.register(Marca)

admin.site.register(Categoria)
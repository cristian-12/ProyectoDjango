from django.contrib import admin

# Register your models here.
# Importamos cada unas de las clases creadas en el archivo models.py
from .models import Etnia
from .models import tipoDoc
from .models import EstaCivil
from .models import TipoEstu
from .models import TipoLogr

admin.site.register(Etnia)
admin.site.register(tipoDoc)
admin.site.register(EstaCivil)
admin.site.register(TipoEstu)
admin.site.register(TipoLogr)

# class EtniaModelAdmin(admin.ModelAdmin):
# 	# indicamos que columnas queremos ver
# 	list_display = ["NombEtnia"]

# 	# indicamos que columnas hacemos clic para editar

# 	# agregamos  una barra de busqueda
# 	search_fields = ["NombEtnia"]
# 	# podemos agregar un filtro 
# 	list_filter = ["NombEtnia"]

# 	class Meta:
# 		model = Etnia
# 	admin.site.register(Etnia)

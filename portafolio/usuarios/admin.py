from django.contrib import admin

# Register your models here.

from .models import Usuarios, Experiencia, Educacion, Habilidades, Logros

class UsuariosModelAdmin(admin.ModelAdmin):
	# Indicamos que columnas queremos ver:
	list_display = ("__str__", "IdUsuario", "ImagUsua", "EstaUsua")
	# Agregamos una barra de busqueda:
	search_fields = ('IdUsuario', 'GeneUsua','CeluUsua','TeleUsua',)
	# Podemos agregar un filtro:
	list_filter = ('IdUsuario','GeneUsua')
	# Mostramos las fechas de creacion del usuario:
	readonly_fields = ('RegiUsua',)
	# Indicamos desde donde se obtienen estos parametros:
	class Meta:
		model = Usuarios
admin.site.register(Usuarios, UsuariosModelAdmin)

class ExperienciaModelAdmin(admin.ModelAdmin):
	# Indicamos que columnas queremos ver:
	list_display = ("__str__", "CargExp", "EmprExpe", "FechInic", "FechaFin" "SopoExpe")
	# Agregamos una barra de busqueda:
	search_fields = ('CargExp','EmprExpe',)
	# Podemos agregar un filtro:
	list_filter = ('CargExp','FechaFin',)
	# Mostramos la fecha de creacion del usuario:
	readonly_fields  = ('EstaExpt',)
	# Indicamos desde donde se obtienen estos parametros:
	class Meta:
		model = Experiencia
admin.site.register(Experiencia, ExperienciaModelAdmin)

class EducacionModelAdmin(admin.ModelAdmin):
	# Indicamos que columnas queremos ver:
	list_display = ("__str__", "TipoEstu", "TituloEst", "FechGrado", "Instituto", "SopoExpe")
	# Agregamos una barra de busqueda:
	search_fields = ('TituloEst', 'TipoEstu',)
	# Podemos agregar un filtro:
	list_filter = ('TipoEstu', 'FechGrado',)
	# Mostramos las fechas de creacion del usuario:
	readonly_fields = ('EstaUsua',)
	# Indicamos desde donde se obtienen estos parametros:
	class Meta:
		model = Educacion
admin.site.register(Educacion, EducacionModelAdmin)

class LogrosModelAdmin(admin.ModelAdmin):
	# Indicamos que columnas queremos ver:
	list_filter = ("__str__", "NombLogr", "FechLogr", "NombTilo")
	# Agregamos una barra de busqueda:
	search_fields = ('NombLogr','NombTilo','FechLogr',)
	# podemos agregar un filtro:
	list_filter = ('NombTilo','FechLogr','NombLogr',)
	# Mostramos las fechas de creacion del usuario
	# readonly_fields = ('EstaUsua')
	# Indicamos desde donde se obtienen estos parametros:
	class Meta:
		model = Logros
admin.site.register(Logros, LogrosModelAdmin)

class HabilidadesModelAdmin(admin.ModelAdmin):
	# Indicamos que columnas queremos ver:
	list_display = ("__str__", "NombHabil", "NivelHabil")
	# Agregamos una barra de busqueda:
	search_fields = ('NombHabil','NivelHabil',)
	# Podemos agregar un filtro:
	list_filter = ('NivelHabil','NombHabil',)
	# Mostramos las fechas de creacion del usuario:
	# readonly_fields = ('EstaEstu',)
	# Indicamos desde donde se obtienen estos parametros:
	class Meta:
		model = Habilidades
admin.site.register(Habilidades, HabilidadesModelAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Pregunta, ElegirRespuesta, PreguntasRespondidas, QuizUsuario
from .forms import ElegirInlineFormset

class PerfilAdmin(UserAdmin):
    search_fields = ['username', 'first_name', 'last_name']
    list_display = ['username', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'last_login']
    list_filter = ['last_login']
    list_order = ['username']
    fieldsets = (('Usuario',{'fields': ('username', 'password')}), ('Información Personal',
        {'fields': ('first_name', 'last_name', 'email',)}),
        ('Permisos',{'fields': ('is_active','is_staff','is_superuser',)}),)

class ElegirRespuestaInline(admin.TabularInline):
	model = ElegirRespuesta
	can_delete =False
	max_num = ElegirRespuesta.MAXIMO_RESPUESTA
	min_num = ElegirRespuesta.MAXIMO_RESPUESTA
	formset = ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
	model = Pregunta
	inlines = (ElegirRespuestaInline, )
	list_display = ['texto',]
	search_fields = ['texto', 'preguntas__texto']


class PreguntasRespondidasAdmin(admin.ModelAdmin):
	list_display = ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

	class Meta:
		model = PreguntasRespondidas


admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(QuizUsuario)
admin.site.unregister(User)
admin.site.register(User, PerfilAdmin)
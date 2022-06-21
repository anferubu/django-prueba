from django.contrib import admin

from rangefilter.filters import DateRangeFilter
from admin_numeric_filter.admin import (
    NumericFilterModelAdmin,
    RangeNumericFilter
)

from .models import (
    Administrativo,
    Comunidad,
    Especializado,
    Nino,
    Objetivo,
    Profesional,
    ProyAdmon,
    ProyEsp,
    Proyecto,
    Representante
)


@admin.register(Administrativo)
class AdministrativoAdmin(admin.ModelAdmin):
    list_display = ['profesional']

@admin.register(Comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'etnia', 'poblacion', 'representante', 'age_average']

    def age_average(self, obj):
        from django.db.models import Avg
        print(obj)
        result = Nino.objects.filter(comunidad=obj.pk).aggregate(Avg('edad'))
        return round(result['edad__avg'], 2)

    age_average.short_description = 'Edad promedio de niños'

@admin.register(Especializado)
class EspecializadoAdmin(admin.ModelAdmin):
    list_display = ['profesional', 'especializacion']
    list_filter = ['especializacion']

@admin.register(Nino)
class NinoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'edad', 'genero', 'comunidad']
    list_filter = ['comunidad']

@admin.register(Objetivo)
class ObjetivoAdmin(admin.ModelAdmin):
    list_display = ['proyecto', 'descripcion', 'cumplimiento']
    list_filter = ['proyecto']

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'cargo', 'salario']

@admin.register(ProyAdmon)
class ProyAdmonAdmin(admin.ModelAdmin):
    list_display = ['proyecto', 'profesional', 'responsable']
    list_filter = ['responsable']
    search_fields = ['profesional__profesional__nombre', 'profesional__profesional__apellido']

@admin.register(ProyEsp)
class ProyEspAdmin(admin.ModelAdmin):
    list_display = ['proyecto', 'profesional', 'tarea', 'duracion']
    list_filter = ['proyecto']

@admin.register(Proyecto)
class ProyectoAdmin(NumericFilterModelAdmin):
    search_fields = ['titulo']
    search_help_text = 'Buscar por título del proyecto'
    list_display = ['titulo', 'comunidad', 'descripcion', 'presupuesto', 'fecha_inicio', 'fecha_fin', 'tema', 'eval']
    list_filter = ['comunidad', ('evaluacion', RangeNumericFilter), ('fecha_inicio', DateRangeFilter), ('fecha_fin', DateRangeFilter)]

    def eval(self, obj):
        from django.db.models import Avg
        print(obj)
        result = Objetivo.objects.filter(proyecto=obj.pk).aggregate(Avg('cumplimiento'))
        return round(result['cumplimiento__avg'], 2)

    eval.short_description = 'Eval. final'

@admin.register(Representante)
class RepresentanteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'apellido', 'direccion', 'telefono', 'email']
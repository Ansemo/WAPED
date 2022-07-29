from django.contrib import admin
from apps.Elementos.models import ElementoDeportivo,EstadoElemento,Categoria,SubCategoria,Prestamo,HorasDisponible,Devolu

admin.site.register(ElementoDeportivo)
admin.site.register(EstadoElemento)
admin.site.register(HorasDisponible)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Prestamo)
admin.site.register(Devolu)

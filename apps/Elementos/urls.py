from django.urls import path, re_path
from apps.Elementos.views import ListarElementos, RegistrarElemento, EditarElemento, EliminarElementos, \
    RegistrarPrestamo, ListadoElementosdisponibles, DetalleElementosDisponible, AceptarPrestamo,CancelarPrestamo, VistaDevolucion, RegistrarDevolucion, ListaDevolicion
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('listado_Elementos/', ListarElementos.as_view(), name='listar_elementos'),
    path('registrar_elemento/', RegistrarElemento.as_view(), name='registrar_elemento'),
    path('actualizar_elemento/<int:pk>/', EditarElemento.as_view(), name='actualizar_elemento'),
    path('eliminar_elemento/<int:pk>/', EliminarElementos.as_view(), name='eliminar_elementos'),

    # URLS GENERALES
    path('listado-elementos-disponible/', ListadoElementosdisponibles.as_view(), name='listado_elementos_disponible'),
    path('detalle_elemento/<int:pk>/', DetalleElementosDisponible.as_view(), name='detalle_elemento'),
    path('registrar_prestamo/', RegistrarPrestamo.as_view(), name='registrar_prestamo'),
    path('aceptar-prestamo/<int:pk>',AceptarPrestamo.as_view(),name= 'aceptar_prestamo',),
    path('cancelar-prestamo/<int:pk>',CancelarPrestamo.as_view(),name= 'cancelar_prestamo',),
    path('devolucion/<int:pk>/',VistaDevolucion.as_view(),name= 'vista_devolucion',),
    path('registrar_devolucion/', RegistrarDevolucion.as_view(), name='registrar_devolucion'),
    path('listado-devoluciones/', ListaDevolicion.as_view(), name='listado_devoluciones'),

]
# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$', serve, {
#         'document_root': settings.MEDIA_ROOT,
#     }),
# ]

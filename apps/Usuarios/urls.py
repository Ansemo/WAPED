from django.urls import path, re_path
from apps.Usuarios.views import Inicio, ListadoUsuario, RegistrarUsuario, EditarUsuario, EliminarUsuarios
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('', Inicio.as_view(), name='UsuariInicio'),
    path('listado_usuarios/', ListadoUsuario.as_view(), name='listar_usuario'),
    path('registrar_usuarios/', RegistrarUsuario.as_view(), name='registrar_usuario'),
    path('actualizar_usuarios/<int:pk>/', EditarUsuario.as_view(), name='actualizar_usuario'),
    path('eliminar_usuarios/<int:pk>/', EliminarUsuarios.as_view(), name='eliminar_usuario'),

]
# urlpatterns += [
#     re_path(r'^media/(?P<path>.*)$', serve, {
#         'document_root': settings.MEDIA_ROOT,
#     }),
# ]
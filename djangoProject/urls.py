from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include, re_path
from apps.Usuarios.views import Login, logoutUsuario
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.Usuarios.urls'), name='index'),
    path('Elementos/', include('apps.Elementos.urls'), name='ElementosDeportivoMain'),
    path('accounts/login/', Login.as_view(), name='iniciarsesion'),
    path('logout/', login_required(logoutUsuario), name="logout"),
]
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]

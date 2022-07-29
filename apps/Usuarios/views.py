from django.shortcuts import render, redirect
import json
from django.urls import reverse_lazy
from django.core.serializers import serialize
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from apps.Usuarios.forms import FormularioLogin, FormularioUsuario
from apps.Usuarios.mixins import LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin
from apps.Usuarios.models import Usuario
from apps.Elementos.models import Prestamo, ElementoDeportivo


class Login(FormView):
    """Validar el login de usuario


    :return: Redireccion hacia index
    """
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('UsuariInicio')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        """Validar csrf

        :param request: Recibimos el csrf del usuario a ingresar
        :return: Redireccion hacia index
        """
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    """Cerrar sesion usuario

    :param request: usuario logueado
    :return: Retorna hacia el login
    """
    logout(request)
    return HttpResponseRedirect('/accounts/login/')


class Inicio(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'prestamo/dashboard.html'

    def get_context_data(self, **kwargs):
        datos = {}
        DatosGrafica = {
            'Devuelto': 0,
            'En espera': 0,
            'En curso': 0,
            'cancelado': 0
        }
        context = super().get_context_data(**kwargs)
        context['prestamos'] = Prestamo.objects.all()
        context['prestamos_realizados'] = Prestamo.objects.filter(estado=True, devolucion=True, cancelacion=False)
        context['solicitudes_pendientes'] = Prestamo.objects.filter(estado=False,cancelacion=False)
        context['devolucion_pendientes'] = Prestamo.objects.filter(devolucion=False)
        context['graficosDevuelto'] = Prestamo.objects.filter(estado=True, devolucion=True, cancelacion=False)
        context['graficosEnespera'] = Prestamo.objects.filter(estado=False, devolucion=False)
        context['graficosEncurso'] = Prestamo.objects.filter(estado=True, devolucion=False)
        context['graficosCancelados'] = Prestamo.objects.filter(estado=True, devolucion=True, cancelacion=True)
        context['elementos_deportivos'] = ElementoDeportivo.objects.filter(estado_eliminacion=True)
        return context


class ListadoUsuario(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, ListView):
    permission_required = ('Usuarios.view_usuario',)
    model = Usuario
    template_name = 'usuarios/listar_usuario.html'
    def get_queryset(self):

        return self.model.objects.filter(is_active=True)

    def get(self, request, *args, **kwargs):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return render(request, self.template_name)


class RegistrarUsuario(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, CreateView):
    permission_required = ('Usuarios.add_usuario',)
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'
    success_url = reverse_lazy('listar_usuario')

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            print('ES UNA PETICION AJAX')
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_usuario = Usuario(
                    email=form.cleaned_data.get('email'),
                    username=form.cleaned_data.get('username'),
                    nombres=form.cleaned_data.get('nombres'),
                    apellidos=form.cleaned_data.get('apellidos'),
                    is_studet=form.cleaned_data.get('is_studet'),

                )
                nuevo_usuario.set_password(form.cleaned_data.get('password1'))
                nuevo_usuario.save()

                mensaje = f'{self.model.__name__} registrado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha registrado correctamente'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            print('NO SOY UNA PETICION AJAX')
            return redirect('inicio_usuario')


class EditarUsuario(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, UpdateView):
    permission_required = ('Usuarios.change_usuario',)
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/editar_usuario.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                mensaje = f'{self.model.__name__} actualizado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 201
                return response
            else:
                mensaje = f'{self.model.__name__} no se ha actualizado correctamenta'
                error = form.errors
                response = JsonResponse({'mensaje': mensaje, 'error': error})
                response.status_code = 400
                return response
        else:
            return redirect('inicio_usuario')


class EliminarUsuarios(LoginYStaffMixin, DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar_usuario.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            usuario = self.get_object()
            usuario.is_active = False
            usuario.save()
            mensaje = f'{self.model.__name__} eliminado correctamente'
            error = 'No hay error'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('inicio_usuario')

    # def get_context_data(self, **kwargs):
    #     context = {}
    #     context['object'] = self.object.get(id = self.kwargs['pk'])
    #
    # def get(self,request,*args,**kwargs):
    #     return render(request,self.template_name,self.get_context_data())

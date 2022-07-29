import json
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse, JsonResponse
from apps.Usuarios.models import Usuario
from apps.Elementos.mixins import LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin
from apps.Elementos.models import ElementoDeportivo, Prestamo, Devolu, EstadoElemento
from apps.Elementos.forms import FormularioElementos, FormularioDevolucion

"""
=================== Elementos Deportivos ===================
"""


class ListarElementos(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, ListView):
    permission_required = ('Elementos.view_elementodeportivo',)

    model = ElementoDeportivo
    # context_object_name = 'Elementos'
    template_name = 'Elementos/Listar_Elementos.html'

    def get_queryset(self):
        return self.model.objects.filter(estado_eliminacion=True)

    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            lista_inventario = []
            for inventario in self.get_queryset():
                data_inventario = {}
                data_inventario['id'] = inventario.pk
                data_inventario['numero'] = inventario.numero
                data_inventario['categoria'] = inventario.sub_categoria.categoria.nombre
                data_inventario['sub_categoria'] = inventario.sub_categoria.nombre
                data_inventario['estado'] = inventario.estado.descripcion
                data_inventario['disponivilidad'] = inventario.disponibilidad
                data_inventario['imagen'] = inventario.imagen.url

                lista_inventario.append(data_inventario)
            data = json.dumps(lista_inventario)

            return HttpResponse(data, 'application/json')
        else:
            return render(request, self.template_name)


class RegistrarElemento(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, CreateView):
    permission_required = ('Elementos.add_elementodeportivo',)
    model = ElementoDeportivo
    form_class = FormularioElementos
    template_name = 'Elementos/crear_elemento.html'
    success_url = reverse_lazy('listar_elementos')
    message = 'No tienes permiso para crear nuevos elementos deportivos'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                nuevo_elemento = ElementoDeportivo(
                    numero=form.cleaned_data.get('numero'),
                    imagen=form.cleaned_data.get('imagen'),
                    estado=form.cleaned_data.get('estado'),
                    sub_categoria=form.cleaned_data.get('sub_categoria'),
                    disponibilidad=form.cleaned_data.get('disponibilidad'),

                )
                nuevo_elemento.save()

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
            return redirect('listar_elementos')


class EditarElemento(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, UpdateView):
    permission_required = ('Elementos.change_elementodeportivo',)
    model = ElementoDeportivo
    form_class = FormularioElementos
    template_name = 'Elementos/editar_elemento.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
            if form.is_valid():
                print(form.cleaned_data)
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


class EliminarElementos(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, DeleteView):
    permission_required = ('Elementos.delete_elementodeportivo',)
    model = ElementoDeportivo
    template_name = 'Elementos/eliminar_elemento.html'
    message = 'No tienes permiso para eliminar elementos deportivos'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            elemento = self.get_object()
            elemento.estado_eliminacion = False
            elemento.save()
            mensaje = f'{self.model.__name__} eliminado correctamente'
            error = 'No hay error'
            response = JsonResponse({'mensaje': mensaje, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('listar_elementos')

    # def get_context_data(self, **kwargs):
    #     context = {}
    #     context['object'] = self.object.get(id = self.kwargs['pk'])
    #
    # def get(self,request,*args,**kwargs):
    #     return render(request,self.template_name,self.get_context_data())


"""
=================== End Elementos Deportivos ===================
"""


class AceptarPrestamo(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, UpdateView):
    model = Prestamo
    success_url = reverse_lazy('iniciarsesion')

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            prestamo = Prestamo.objects.filter(id=request.POST.get('prestamo')).first()
            prestamo.estado = True
            prestamo.save()

            mensaje = f'{self.model.__name__} Prestamo aceptado correctamente'
            error = 'No hay error'
            response = JsonResponse({'mensaje': mensaje, 'error': error, 'url': self.success_url})
            response.status_code = 201
            return response

        return redirect('listado_elementos_disponible')


class CancelarPrestamo(LoginYStaffMixin, ValidarPermisosRequeridosUsuariosMixin, UpdateView):
    model = Prestamo
    success_url = reverse_lazy('iniciarsesion')

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            prestamo = Prestamo.objects.filter(id=request.POST.get('prestamo')).first()
            prestamo.cancelacion = True
            prestamo.devolucion = True
            prestamo.estado = True
            prestamo.save()

            elemento = ElementoDeportivo.objects.filter(id=prestamo.elemento_deportivo.id).first()
            elemento.disponibilidad = True
            elemento.save()

            mensaje = f'{self.model.__name__} Prestamo cancelado correctamente'
            error = 'No hay error'
            response = JsonResponse({'mensaje': mensaje, 'error': error, 'url': self.success_url})
            response.status_code = 201
            return response

        return redirect('listado_elementos_disponible')


class ListadoElementosdisponibles(ListView):
    model = ElementoDeportivo
    paginate_by = 8
    template_name = 'prestamo/crear_prestamo.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(disponibilidad=True, estado__nivel_gravedad=1).order_by('sub_categoria')
        return queryset


class DetalleElementosDisponible(DetailView):
    model = ElementoDeportivo
    template_name = 'prestamo/detalle_elemento.html'


class RegistrarPrestamo(CreateView):
    model = Prestamo
    success_url = reverse_lazy('iniciarsesion')

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            elemento = ElementoDeportivo.objects.filter(id=request.POST.get('elemento')).first()
            usuario = Usuario.objects.filter(id=request.POST.get('usuario')).first()
            hora = request.POST.get('hora')
            print(Prestamo.objects.filter(id_estudiante=usuario.id).filter(cancelacion=True))

            if elemento and usuario and len(
                    Prestamo.objects.filter(id_estudiante=usuario.id).filter(devolucion=False)) == 0 and len(
                Prestamo.objects.filter(id_estudiante=usuario.id).filter(estado=False)) == 0:
                nuevo_prestamo = self.model(
                    id_estudiante=usuario,
                    hora_presamto=hora,
                    elemento_deportivo=elemento
                )
                nuevo_prestamo.save()

                mensaje = f'{self.model.__name__} registrado correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error, 'url': self.success_url})
                response.status_code = 201
                return response
            elif len(Prestamo.objects.filter(id_estudiante=usuario.id).filter(estado=False)) > 0:
                mensaje = f'Tienes prestamos en espera'
                response = JsonResponse({'mensaje': mensaje})
                response.status_code = 201
                return response
            elif len(Prestamo.objects.filter(id_estudiante=usuario.id).filter(devolucion=False)) > 0:
                mensaje = f'Tienes devoluciones pendientes'
                response = JsonResponse({'mensaje': mensaje})
                response.status_code = 201
                return response

        return redirect('listado_elementos_disponible')


class VistaDevolucion(UpdateView):
    model = Prestamo
    form_class = FormularioDevolucion
    template_name = 'prestamo/devolucion.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            print(request.POST)
        #     form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
        #     if form.is_valid():
        #         form.save()
        #         mensaje = f'{self.model.__name__} actualizado correctamente'
        #         error = 'No hay error'
        #         response = JsonResponse({'mensaje': mensaje, 'error': error})
        #         response.status_code = 201
        #         return response
        #     else:
        #         mensaje = f'{self.model.__name__} no se ha actualizado correctamenta'
        #         error = form.errors
        #         response = JsonResponse({'mensaje': mensaje, 'error': error})
        #         response.status_code = 400
        #         return response
        # else:
        #     return redirect('inicio_usuario')


class RegistrarDevolucion(CreateView):
    model = Devolu
    success_url = reverse_lazy('iniciarsesion')

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            prestamo = Prestamo.objects.filter(id=request.POST.get('prestamo')).first()
            encargado = Usuario.objects.filter(id=request.POST.get('encargado')).first()
            descripcion = request.POST.get('descripcion')
            estado_entrega = EstadoElemento.objects.filter(id=request.POST.get('estado_entrega')).first()

            if not estado_entrega:
                mensaje = f'El estado de entrega es obligatorio'
                response = JsonResponse({'mensaje': mensaje})
                response.status_code = 201
                return response
            else:
                nueva_devolucion = self.model(
                    prestamo=prestamo,
                    encarcago=encargado,
                    descripcion=descripcion,
                    estado_entrega=estado_entrega,
                )
                nueva_devolucion.save()

                prestamo.devolucion = True
                prestamo.save()

                elemento = ElementoDeportivo.objects.filter(id=prestamo.elemento_deportivo.id).first()
                elemento.disponibilidad = True
                elemento.save()

                mensaje = f'{self.model.__name__} Devolucion aplicada correctamente'
                error = 'No hay error'
                response = JsonResponse({'mensaje': mensaje, 'error': error, 'url': self.success_url})
                response.status_code = 201
                return response

            #     nuevo_prestamo = self.model(
            #         id_estudiante=usuario,
            #         hora_presamto=hora,
            #         elemento_deportivo=elemento
            #     )
            #     nuevo_prestamo.save()
            #     mensaje = f'{self.model.__name__} registrado correctamente'
            #     error = 'No hay error'
            #     response = JsonResponse({'mensaje': mensaje, 'error': error, 'url': self.success_url})
            #     response.status_code = 201
            #     return response
            # elif len(Prestamo.objects.filter(id_estudiante=usuario.id).filter(estado=False)) > 0:
            #     mensaje = f'Tienes en espera prestamos pendientes'
            #     response = JsonResponse({'mensaje': mensaje})
            #     response.status_code = 201
            #     return response
            # elif len(Prestamo.objects.filter(id_estudiante=usuario.id).filter(devolucion=False)) > 0:
            #     mensaje = f'Tienes devoluciones pendientes'
            #     response = JsonResponse({'mensaje': mensaje})
            #     response.status_code = 201
            #     return response

        return redirect('iniciarsesion')


class ListaDevolicion(ListView):
    model = Devolu
    template_name = 'prestamo/lista_devoluciones.html'

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['devoluciones'] = self.get_queryset()
        return context
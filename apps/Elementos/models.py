from django.db import models
from apps.Usuarios.models import Usuario
from django.db.models.signals import post_save
from apps.Usuarios.models import Usuario

class EstadoElemento(models.Model):
    nivel = [
        (1, 'Muy bajo'),
        (2, 'Bajo'),
        (3, 'Moderado'),
        (4, 'Alto'),
        (5, 'Muy alto'),
    ]
    nivel_gravedad = models.IntegerField('Nivel de gravedad', choices=nivel, null=False, blank=False)
    descripcion = models.CharField('Descripcion', max_length=30, null=False, blank=False)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.descripcion


class HorasDisponible(models.Model):
    hora = models.TextField('Hora', max_length=50, null=False, blank=False)
    disponibilidad = models.BooleanField('Estado de disponibilidad', default=True)

    class Meta:
        verbose_name = 'hora'
        verbose_name_plural = 'horas'

    def __str__(self):
        return self.hora


class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre de categoria', max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: 'Categoria'
        verbose_name_plural: 'Categorias'


class SubCategoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=100, unique=True, blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField('Imagen', upload_to='Categoria/', max_length=200, null=True,
                               blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name: 'Sub Categoria'
        verbose_name_plural: 'Sub Categorias'


class ElementoDeportivo(models.Model):

    id = models.AutoField(primary_key=True)
    numero = models.IntegerField('Numero identificador', unique=True, blank=False, null=False)
    imagen = models.ImageField('Imagen', upload_to='Elementos/', max_length=200, null=True,
                               blank=True)
    estado = models.ForeignKey(EstadoElemento, on_delete=models.CASCADE)
    sub_categoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    horas_disponibles = models.ManyToManyField(HorasDisponible)
    disponibilidad = models.BooleanField('Estado de disponibilidad', default=True)
    estado_eliminacion = models.BooleanField(default=True)


    def __str__(self):
        return f'{self.sub_categoria.categoria.nombre} | {self.sub_categoria.nombre} | Numero {self.numero}'



class Prestamo(models.Model):

    id_estudiante = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha_prestamo = models.DateField('Fecha de creacion prestamo', auto_now=True, auto_now_add=False)
    hora_presamto = models.TextField('Hora Prestamo', null=False, blank=False)
    elemento_deportivo = models.ForeignKey(ElementoDeportivo, on_delete=models.CASCADE)
    estado = models.BooleanField('Aceptar prestamo', default=False, null=False, blank=False)
    devolucion = models.BooleanField('Devolucion', default=False, null=False, blank=False)
    cancelacion = models.BooleanField('Cancelar prestamo ', default=False, null=True, blank=True)

    class Meta:
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'

    def __str__(self):
        return f'Numero: {self.pk} Id estudiante: {self.id_estudiante}'


class Devolu(models.Model):
    prestamo = models.ForeignKey(Prestamo,on_delete=models.CASCADE)
    encarcago = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    fecha_devolucion = models.DateTimeField('Fecha y hora de devolucion', auto_now=True, auto_now_add=False)
    descripcion = models.CharField('Descripcion',max_length=200,null=False,blank=False)
    estado_entrega = models.ForeignKey(EstadoElemento,on_delete=models.CASCADE)


def cambiar_estado_elemento_false(sender, instance, **kwargs):

    if instance.elemento_deportivo.disponibilidad == True:
        elemento = ElementoDeportivo.objects.filter(id=instance.elemento_deportivo.id)
        for eleme in elemento:
            eleme.disponibilidad = False
            eleme.save()
    else:
        pass


def senderpruba(sender, instance, **kwargs):
    estudiante = Usuario.objects.filter(id=instance.id_estudiante.id)
    print(estudiante)



post_save.connect(cambiar_estado_elemento_false, sender=Prestamo)
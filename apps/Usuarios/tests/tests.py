import pytest
from apps.Usuarios.models import Usuario, curso
from apps.Elementos.models import *

@pytest.mark.django_db
def test_creacion_devolucion():
    nueva_devolucion= Devolu(
        prestamo=Prestamo.objects.filter(id=2).first(),
        encarcago=Usuario.objects.filter(id=2).first(),
        descripcion='qwerty',
        estado_entrega=EstadoElemento.objects.filter(id=1).first()
    )
    assert nueva_devolucion

@pytest.mark.django_db
def test_creacion_prestamo():
    nuevo_prestamo= Prestamo(
        id_estudiante=Usuario.objects.filter(id=2).first(),
        hora_presamto='12:30PM',
        elemento_deportivo=ElementoDeportivo.objects.filter(id=2).first(),
    )
    assert nuevo_prestamo

@pytest.mark.django_db
def test_creacion_subcategoriao():
    nueva_sub_categoria = Categoria(
        nombre='Balon'
    )
    assert nueva_sub_categoria

@pytest.mark.django_db
def test_creacion_elemento():
    nueva_sub_categoria = SubCategoria(
        nombre='Voleibol',
        categoria=Categoria.objects.filter(nombre='Balon').first()
    )
    assert nueva_sub_categoria

@pytest.mark.django_db
def test_creacion_elemento():
    nuevo_elemento = ElementoDeportivo(
        numero=12,
        estado=EstadoElemento.objects.filter(descripcion='Buen estado').first(),
        sub_categoria=SubCategoria.objects.filter(nombre='Baloncesto').first()
    )
    assert nuevo_elemento

@pytest.mark.django_db
def test_creacion_super_usuario():
    usuario = Usuario.objects.create_superuser(
        nombres='Angel',
        email='segura139921@gmail.com',
        password='q1w2e3r4t5y6',
        username='Ansemo666'
    )
    assert usuario.is_superuser

@pytest.mark.django_db
def test_creacion_super_usuario():
    usuario = Usuario.objects.create_superuser(
        nombres='Angel',
        email='segura139921@gmail.com',
        password='q1w2e3r4t5y6',
        username='Ansemo666'
    )
    assert usuario.is_superuser

@pytest.mark.django_db
def test_creacion_estudiante():
    usuario = Usuario.objects.create_student(
        nombres='Angel',
        email='segura139921@gmail.com',
        password='q1w2e3r4t5y6',
        username='Ansemo666',
        curso=curso.objects.filter(nombre='11A').first()
    )
    assert usuario.is_studet

@pytest.mark.django_db
def test_creacion_administrador():
    usuario = Usuario.objects.create_user_admin(
        nombres='Angel',
        email='segura139921@gmail.com',
        password='q1w2e3r4t5y6',
        username='Ansemo666',
    )
    assert usuario.is_staff

@pytest.mark.django_db
def test_creacion_super_usuario():
    nuevo_curso = curso(
        nombre='11B'
    )
    assert nuevo_curso.nombre == '11B'

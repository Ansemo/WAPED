from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):

    def _create_user(self, username, email, nombres, curso, password, is_staff, is_superuser, is_studet,
                     **extra_fields):
        user = self.model(
            username=username,
            email=email,
            nombres=nombres,
            curso=curso,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_studet=is_studet,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user_admin(self, username, email, nombres, password=None, **extra_fields):
        return self._create_user(username, email, nombres,None, password, True, False, True, **extra_fields)

    def create_student(self, username, email, nombres, curso, password=None, **extra_fields):
        return self._create_user(username, email, nombres, curso, password, False, False, True, **extra_fields)

    def create_superuser(self, username, email, nombres, password=None, **extra_fields):
        return self._create_user(username, email, nombres, None, password, True, True, True, **extra_fields)


class curso(models.Model):
    nombre = models.CharField('Nombre del curso', max_length=100, null=False, blank=False)


    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nombre


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electronico', unique=True, max_length=255)
    nombres = models.CharField('Nombre', max_length=100, blank=True, null=True)
    apellidos = models.CharField('Apellidos', max_length=100, blank=True, null=True)
    curso = models.ForeignKey(curso, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField('Imagen de prefil', upload_to='usuario/', max_length=200,
                               blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField('Es administrador?',default=False)
    is_studet = models.BooleanField('Es estudiante?',default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres']

    class Meta:
        verbose_name: 'Usuario'
        verbose_name_plural: 'Usuarios'

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

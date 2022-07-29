# Generated by Django 4.0.5 on 2022-06-20 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Elementos', '0003_alter_elementodeportivo_imagen_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hora_prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.DateTimeField(auto_now_add=True, verbose_name='Hora de prestamo')),
                ('estado', models.BooleanField(default=True, verbose_name='Hora prestamo')),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(auto_now_add=True, verbose_name='Fecha de prestamo')),
                ('elemento_deportivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elementos.elementodeportivo')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hora_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Elementos.hora_prestamo')),
            ],
            options={
                'verbose_name': 'Prestamo',
                'verbose_name_plural': 'Prestamos',
            },
        ),
    ]

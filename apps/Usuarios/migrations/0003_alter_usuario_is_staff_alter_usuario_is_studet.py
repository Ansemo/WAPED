# Generated by Django 4.0.5 on 2022-06-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_alter_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Es administrador?'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='is_studet',
            field=models.BooleanField(default=False, verbose_name='Es estudiante?'),
        ),
    ]

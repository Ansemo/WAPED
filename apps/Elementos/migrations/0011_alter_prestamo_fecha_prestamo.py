# Generated by Django 4.0.5 on 2022-06-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0010_prestamo_hora_presamto_alter_prestamo_fecha_prestamo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de prestamo'),
        ),
    ]
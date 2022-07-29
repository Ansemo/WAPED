# Generated by Django 4.0.5 on 2022-06-23 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0017_remove_prestamo_estudiante_prestamo_id_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementodeportivo',
            name='estado_eliminacion',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='hora_presamto',
            field=models.IntegerField(choices=[(1, '12:00PM - 12:30PM'), (2, '03:00PM - 03:30PM')], verbose_name='Hora Prestamo'),
        ),
    ]
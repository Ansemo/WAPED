# Generated by Django 4.0.5 on 2022-07-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0035_elementodeportivo_cantidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementodeportivo',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='elementodeportivo',
            name='hora_presamto',
            field=models.IntegerField(choices=[[1, '12:00PM - 12:30PM'], [2, '03:00PM - 03:30PM']], default=2, verbose_name='Hora Prestamo'),
            preserve_default=False,
        ),
    ]

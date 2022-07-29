# Generated by Django 4.0.5 on 2022-06-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0006_alter_prestamo_fecha_prestamo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='hora_prestamo',
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateTimeField(unique_for_date=True, verbose_name='Fecha de prestamo'),
        ),
        migrations.DeleteModel(
            name='Hora_prestamo',
        ),
    ]
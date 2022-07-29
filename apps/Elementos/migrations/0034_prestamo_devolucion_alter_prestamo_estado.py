# Generated by Django 4.0.5 on 2022-07-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0033_prestamo_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='devolucion',
            field=models.BooleanField(default=False, verbose_name='Estado devolucion'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='estado',
            field=models.BooleanField(default=False, verbose_name='Estado del prestamo'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-05 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0036_remove_elementodeportivo_cantidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementodeportivo',
            name='hora_presamto',
        ),
    ]
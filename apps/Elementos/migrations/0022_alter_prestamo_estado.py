# Generated by Django 4.0.5 on 2022-07-01 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0021_alter_elementodeportivo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='estado',
            field=models.BooleanField(default=False, verbose_name='Estado'),
        ),
    ]
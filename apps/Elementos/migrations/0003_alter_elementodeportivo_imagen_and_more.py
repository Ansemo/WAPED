# Generated by Django 4.0.5 on 2022-06-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0002_rename_elemento_deportivo_elementodeportivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementodeportivo',
            name='imagen',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='static/Elemento_deportivo/Elementos/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='imagen',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='static/Elemento_deportivo/Categorias/', verbose_name='Imagen'),
        ),
    ]

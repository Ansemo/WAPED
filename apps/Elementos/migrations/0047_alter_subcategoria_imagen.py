# Generated by Django 4.0.5 on 2022-07-16 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0046_remove_devolu_imagen_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategoria',
            name='imagen',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='Categoria/', verbose_name='Imagen'),
        ),
    ]
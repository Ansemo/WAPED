# Generated by Django 4.0.5 on 2022-07-12 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0045_rename_imagen_devolu_imagen_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devolu',
            name='imagen_estado',
        ),
    ]

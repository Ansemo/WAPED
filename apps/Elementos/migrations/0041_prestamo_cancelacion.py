# Generated by Django 4.0.5 on 2022-07-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elementos', '0040_devolu'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='cancelacion',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Estado cancelacion'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-20 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Elementos', '0012_alter_prestamo_fecha_prestamo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestamo',
            name='id_estudiante',
        ),
        migrations.AddField(
            model_name='prestamo',
            name='estudiante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
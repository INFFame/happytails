# Generated by Django 5.0.6 on 2024-05-13 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_alter_estadocivil_descripcion_estado_civil_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('hora_cita', models.TimeField(blank=True, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.paciente')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sucursal')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.veterinario')),
            ],
        ),
    ]

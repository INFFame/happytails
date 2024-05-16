# Generated by Django 5.0.6 on 2024-05-13 06:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comuna', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especialidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_estado_civil', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RazaPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza_paciente', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_tratamiento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('numrut_cliente', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('dvrut_cliente', models.CharField(max_length=2)),
                ('telefono_cliente', models.CharField(max_length=15)),
                ('direccion_cliente', models.CharField(max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comuna')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.estadocivil')),
            ],
        ),
        migrations.CreateModel(
            name='Recepcionista',
            fields=[
                ('numrut_recepcionista', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('dvrut_recepcionista', models.CharField(max_length=2)),
                ('nombre_recepcionista', models.CharField(max_length=50)),
                ('apellido_recepcionista', models.CharField(max_length=50)),
                ('direccion_recepcionista', models.CharField(max_length=50)),
                ('telefono_recepcionista', models.CharField(max_length=15)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comuna')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.estadocivil')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.region'),
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_clinica', models.CharField(max_length=50)),
                ('direccion_clinica', models.CharField(max_length=200)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_paciente', models.CharField(max_length=50)),
                ('raza_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.razapaciente')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_paciente', models.CharField(max_length=50)),
                ('sexo_paciente', models.BooleanField()),
                ('fecha_nacimiento_paciente', models.DateField()),
                ('color_paciente', models.CharField(max_length=25)),
                ('observacion_paciente', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
                ('tipo_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipopaciente')),
                ('tipo_tratamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tratamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Veterinario',
            fields=[
                ('numrut_veterinario', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('dvrut_veterinario', models.CharField(max_length=2)),
                ('nombre_veterinario', models.CharField(max_length=50)),
                ('apellido_veterinario', models.CharField(max_length=50)),
                ('direccion_veterinario', models.CharField(max_length=50)),
                ('telefono_veterinario', models.CharField(max_length=15)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.comuna')),
                ('especialidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.especialidad')),
                ('estado_civil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.estadocivil')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

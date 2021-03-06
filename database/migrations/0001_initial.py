# Generated by Django 4.0.5 on 2022-06-20 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'administrativo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('etnia', models.CharField(blank=True, max_length=25, null=True)),
                ('poblacion', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comunidad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Especializado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especializacion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'especializado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nino',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('genero', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'nino',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('cumplimiento', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'objetivo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('cargo', models.CharField(max_length=50)),
                ('salario', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'profesional',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProyAdmon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsable', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'proy_admon',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('alcance', models.CharField(blank=True, max_length=150, null=True)),
                ('presupuesto', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('tema', models.CharField(blank=True, max_length=50, null=True)),
                ('evaluacion', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'proyecto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProyEsp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('duracion', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'proy_esp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'representante',
                'managed': False,
            },
        ),
    ]

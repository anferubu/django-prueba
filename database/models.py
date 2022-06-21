# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrativo(models.Model):
    profesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='profesional', blank=True, null=True)

    def __str__(self):
        return f'{self.profesional}'

    class Meta:
        managed = False
        db_table = 'administrativo'


class Comunidad(models.Model):
    representante = models.ForeignKey('Representante', models.DO_NOTHING, db_column='representante', blank=True, null=True)
    nombre = models.CharField(max_length=25)
    etnia = models.CharField(max_length=25, blank=True, null=True)
    poblacion = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}'

    class Meta:
        managed = False
        db_table = 'comunidad'


class Especializado(models.Model):
    profesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='profesional', blank=True, null=True)
    especializacion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.profesional}'

    class Meta:
        managed = False
        db_table = 'especializado'


class Nino(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    comunidad = models.ForeignKey(Comunidad, models.DO_NOTHING, db_column='comunidad')
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField(blank=True, null=True)
    genero = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        managed = False
        db_table = 'nino'


class Objetivo(models.Model):
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='proyecto')
    descripcion = models.CharField(max_length=100)
    cumplimiento = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.proyecto} - {self.descripcion} ({self.cumplimiento})'

    class Meta:
        managed = False
        db_table = 'objetivo'


class Profesional(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    cargo = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        managed = False
        db_table = 'profesional'


class ProyAdmon(models.Model):
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='proyecto')
    profesional = models.ForeignKey(Administrativo, models.DO_NOTHING, db_column='profesional')
    responsable = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f'{self.profesional} ({self.proyecto})'

    class Meta:
        managed = False
        db_table = 'proy_admon'


class ProyEsp(models.Model):
    proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='proyecto')
    profesional = models.ForeignKey(Especializado, models.DO_NOTHING, db_column='profesional')
    tarea = models.CharField(unique=True, max_length=100, blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.profesional} ({self.proyecto})'

    class Meta:
        managed = False
        db_table = 'proy_esp'


class Proyecto(models.Model):
    comunidad = models.ForeignKey(Comunidad, models.DO_NOTHING, db_column='comunidad')
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    alcance = models.CharField(max_length=150, blank=True, null=True)
    presupuesto = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    tema = models.CharField(max_length=50, blank=True, null=True)
    evaluacion = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.titulo}'

    class Meta:
        managed = False
        db_table = 'proyecto'


class Representante(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    class Meta:
        managed = False
        db_table = 'representante'

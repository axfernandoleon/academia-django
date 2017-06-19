# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Estudiante(models.Model):
    id_estudiante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    cedula = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'

    def __unicode__(self):
        return "%s - %s -%s" % (self.id_estudiante, self.nombre, self.apellido)


class Materia(models.Model):
    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materia'

    def __unicode__(self):
        return "%s - %s" % (self.id_materia, self.nombre)


class Paralelo(models.Model):
    id_paralelo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    la_materia = models.ForeignKey(Materia, db_column='la_materia', blank=True, null=True)
    la_periodo = models.ForeignKey('Periodo', db_column='la_periodo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paralelo'

    def __unicode__(self):
        return "%s - %s - %s" % (self.id_paralelo, self.nombre, self.la_periodo.nombre)


class ParaleloEstudiante(models.Model):
    id_paralelo_estudiante = models.AutoField(primary_key=True)
    la_paralelo = models.ForeignKey(Paralelo, db_column='la_paralelo', blank=True, null=True)
    la_estudiante = models.ForeignKey(Estudiante, db_column='la_estudiante', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paralelo_estudiante'

    def __unicode__(self):
        return "%s - %s" % (self.la_paralelo, self.la_estudiante)


class Periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodo'

    def __unicode__(self):
        return "%s" % (self.nombre)

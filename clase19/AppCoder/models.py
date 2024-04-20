from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}   Camada: {self.camada}"


class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    carrera = models.CharField(max_length=25)
    email = models.CharField(max_length=25)

    def __str__(self):
        return f"Nombre: {self.nombre}  Edad: {self.edad}  Carrera: {self.carrera}  Email: {self.email}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    legajo = models.IntegerField()
    edad = models.IntegerField()
    tutor = models.CharField(max_length=25)
    email = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre}   Legajo: {self.legajo}   Edad: {self.edad}  Carrera: {self.carrera}  Email: {self.email}"
    

class Avatar(models.Model):
    User = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True , blank=True)

    def __str__(self):
        return f"User: {self.User}  -  Imagen: {self.imagen}"
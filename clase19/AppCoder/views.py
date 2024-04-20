from django.shortcuts import render
from AppCoder.models import Curso,Avatar
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario, UserEditForm
from AppCoder.models import Alumno
from AppCoder.forms import Alumno_formulario
from AppCoder.forms import Profesor_formulario
from AppCoder.models import Profesor
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.



def inicio(request):
    return render( request , "padre.html")



def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

@login_required
def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def curso_formulario(request):

    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre=datos["nombre"] , camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")


    return render(request , "formulario.html")


def buscar_curso(request):

    return render(request, "buscar_curso.html")


def buscar(request):

    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains= nombre)
        return render(request, "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")
    


@login_required
def alumnos(request):
    alumno = Alumno.objects.all()
    print(alumnos)
    dicc = {"alumnos": alumno}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)
    



def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            alumno = Alumno(nombre=datos["nombre"] , edad=datos["edad"] , carrera=datos["carrera"] , email=datos["email"])
            alumno.save()
            return render(request , "formulario_alumnos.html")

    return render(request, "formulario_alumnos.html")


@login_required
def profesores(request):
    profesor = Profesor.objects.all()
    print(profesores)
    dicc = {"profesores": profesor}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)


def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            profesor = Profesor(nombre=datos["nombre"] , legajo=datos["legajo"] , edad=datos["edad"] ,tutor=datos["tutor"] , email=datos["email"])
            profesor.save()
            return render(request , "formulario_profesores.html")
    else:
        mi_formulario = Profesor_formulario()

    profesores = Profesor_formulario.objects.all()
    return render(request, "formulario_profesores.html")
    






def elimina_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()

    curso = Curso.objects.all()
    return render(request , "cursos.html", {"cursos":curso})


def editar(request, id):
    curso = Curso.objects.get(id=id)
    
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()

            curso = Curso.objects.all()

            return render(request, "cursos.html" , {"cursos":curso})
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})

    return render(request , "editar_curso.html",{"mi_formulario":mi_formulario , "curso":curso})


def elimina_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()

    alumno = Alumno.objects.all()
    return render(request , "alumnos.html", {"alumnos":alumno})



def editar_alumno(request, id):
    
    alumno = Alumno.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario = Alumno_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.edad = datos["edad"]
            alumno.carrera = datos["carrera"]
            alumno.email = datos["email"]
            alumno.save()

            alumno = Alumno.objects.all()
            return render(request , "alumnos.html" , {"alumnos":alumno})
    else:
        mi_formulario = Alumno_formulario(initial={"nombre":alumno.nombre ,  "edad":alumno.edad , "carrera":alumno.carrera , "email":alumno.email})

    return render( request , "editar_alumno.html" , {"mi_formulario": mi_formulario , "alumno":alumno})



def elimina_profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    profesor.delete()

    profesor = Profesor.objects.all()
    return render(request , "profesores.html", {"profesores":profesor})


def editar_profesor(request, id):
    
    profesor = Profesor.objects.get(id=id)

    if request.method == "POST":
        
        mi_formulario = Profesor_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.legajo = datos["legajo"]
            profesor.edad = datos["edad"]
            profesor.tutor = datos["tutor"]
            profesor.email = datos["email"]
            profesor.save()

            profesor = Profesor.objects.all()
            return render(request , "profesores.html" , {"profesores":profesor})
    else:
        mi_formulario = Profesor_formulario(initial={"nombre":profesor.nombre ,  "edad":profesor.legajo , "edad":profesor.edad , "tutor":profesor.tutor , "email":profesor.email})

    return render( request , "editar_profesor.html" , {"mi_formulario": mi_formulario , "profesor":profesor})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contraseña)

            if user is not None:
                login(request , user)
                avatares = Avatar.objects.filter(User=request.user.id)
                return render(request , "inicio.html", {"url":avatares[0].imagen.url,"mensaje":f"Bienvenido/a {usuario}", "usuario":usuario })
            else:
                return HttpResponse(f"Usuario no encontrado")
        else:
            return HttpResponse(f"FORM INCORRECTO {form}")


    form = AuthenticationForm()
    return render(request , "login.html" , {"form":form})


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
        return render(request, "registro.html", {"form":form})
    

def editarPerfil(request):

    usuario = request.user

    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")

    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    return render(request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})

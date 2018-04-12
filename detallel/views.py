from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
# Create your views here.
from django.contrib.auth.decorators import login_required

def listarTemplate(request):
	if request.user.is_authenticated:
		lista=PrincipalPage.objects.all()
		return render(request, 'listarTemplate.html',{'lista': lista})
	else:
		return redirect("login")

def editTemplate(request, id):
	if request.user.is_authenticated:
		template = PrincipalPage.objects.get(id=id)
		if request.POST:
			form=TemplateForm(request.POST, request.FILES, instance=template)
			if form.is_valid():
				form.save()
				return redirect('listarTemplate')
		else:
			form=TemplateForm(instance=template)
			templa = 'editarTemplate.html'
			book = {'form':form}
			return render(request, templa, book)
	else:
		return redirect('login', permanent=False)

def base(request):
	if request.user.is_authenticated:
		dict={}
		return  render(request,"base.html",dict)
	else:
		return redirect("login")


def acceder(request):
	dict={}
	if request.user.is_authenticated:
		return redirect("base")
	else:
		return render(request,"login.html",dict)


def cerrar_sesion(request):
    logout(request)
    return redirect("login")


def iniciar_sesion(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("base")
        else:
            dict = {
                "mensaje": " El usuario o la contraseña son incorrectas!"
            }
            return render(request, "login.html", dict)
    else:
        return redirect("vistasPage")


def vistasPage(request):
	dict={}
	dict["comparar"]=PrincipalPage.objects.all()
	if dict["comparar"]:
		datos=PrincipalPage.objects.all()[:1].get()
		dict["titulo"]=datos.titulo
		dict["fondo"]=datos.fondo
		dict["fondomovil"]=datos.fondomovil
		dict["imagen"]=datos.imagen
		dict["vistas"]=imagenVista.objects.all()
		return render(request, 'view.html',dict)
	else:
		return render(request, '404.html',dict)


def detalleVista(request,id):
	dict={}
	dict["comparar"]=imagenVista.objects.all()
	if dict["comparar"]:
		datos=imagenVista.objects.get(id=id)
		dict["tituloPage"]=datos.titulo
		dict["vistas"]=detalleImagen.objects.filter(imagenVistaDetalle=id)
		print(dict["vistas"])
		return render(request, 'detalle.html',dict)
	else:
		return render(request, '404.html',dict)

def vermas(request,id):
	dict={}
	datos = detalleImagen.objects.get(idPagina=id)
	dict["tituloPage"] = datos.titulo
	dict["descripcion"]= datos.descripcion
	dict["imagen"] = datos.imagen
	return render(request, 'vermas.html',dict)





def agregarVistas(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			form = VistaForm(request.POST, request.FILES)
			if form.is_valid():
				vista = form.save()
				return redirect('listarVistas')
		form = VistaForm()
		return render(request, 'agregaVista.html', {'form': form})
	else:
		return redirect('login', permanent=False)


def agregarContenido(request, id):
	if request.user.is_authenticated:
		imagenvista = imagenVista.objects.get(id=id)
		nv=detalleImagen.objects.filter(imagenVistaDetalle=id)
		idPagina = len(nv) + 1
		if request.method == "POST":
			form = ContenidoForm(request.POST, request.FILES)
			if form.is_valid():

				contenido = form.save(commit=False)
				contenido.imagenVistaDetalle =imagenvista
				contenido.idPagina=idPagina
				contenido.save()
		form = ContenidoForm()
		return render(request, 'agregarContenido.html', {'form':form, 'imagenvista':imagenvista,'idPagina':idPagina})
	else:
		return redirect('listarVistas', permanent=False)



def listarVistas(request):
	if request.user.is_authenticated:
		lista=imagenVista.objects.all()
		return render(request, 'listarVista.html',{'lista': lista})
	else:
		return redirect("login")


def eliminarVista(request, id):
	if request.user.is_authenticated:
		vista = imagenVista.objects.get(id=id)
		if request.POST:
			vista.delete()
			return redirect('listarVistas')
		else:
			template = 'eliminarVista.html'
			book = {'vista':vista}
			return render(request, template, book)
	else:
		return redirect('login', permanent=False)

def editVista(request, id):
	if request.user.is_authenticated:
		vistas = imagenVista.objects.get(id=id)
		if request.POST:
			form=VistaForm(request.POST, request.FILES, instance=vistas)
			if form.is_valid():
				form.save()
				return redirect('listarVistas')
		else:
			form=VistaForm(instance=vistas)
			templa = 'editarVista.html'
			book = {'form':form}
			return render(request, templa, book)
	else:
		return redirect('login', permanent=False)


from django.shortcuts import render, redirect
from core.forms import ProductoForm
from core.forms import DescuentosForm
from core.models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home (request):
    return render(request, 'core/index.html')
    
def compra (request):
    return render(request, 'core/compra.html')

def eliminar1 (request):
    return render(request, 'core/eliminar1.html')

def flores1 (request):
    return render(request, 'core/flores1.html')

def flores2 (request):
    return render(request, 'core/flores2.html')

def flores3 (request):
    return render(request, 'core/flores3.html')

def flores4 (request):
    return render(request, 'core/flores4.html')

def flores5 (request):
    return render(request, 'core/flores5.html')

def flores6 (request):
    return render(request, 'core/flores6.html')

def sesion (request):
    return render(request, 'core/iniciosesion.html')

def mace1 (request):
    return render(request, 'core/mace1.html')

def mace2 (request):
    return render(request, 'core/mace2.html')

def mace3 (request):
    return render(request, 'core/mace3.html')

def mace4 (request):
    return render(request, 'core/mace4.html')

def mace5 (request):
    return render(request, 'core/mace5.html')

def maceteros (request):
    return render(request, 'core/maceteros.html')

def miscompras (request):
    return render(request, 'core/miscompras.html')

def nosotros (request):
    return render(request, 'core/nosotros.html')

def plantas (request):
    return render(request, 'core/plantas.html')

def des (request):
    return render(request, 'core/des.html')

def susc (request):
    return render(request, 'core/susc.html')


def registro (request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect(to="sesion")

    return render(request, 'core/registro.html', {'form':UserCreationForm()})

def sus (request):
    return render(request, 'core/sus.html')

def suscripcion (request):
    return render(request, 'core/suscripcion.html')

def tierra (request):
    return render(request, 'core/tierra.html')

def tierra1 (request):
    return render(request, 'core/tierra1.html')

def tierra2 (request):
    return render(request, 'core/tierra2.html')

def tierra3 (request):
    return render(request, 'core/tierra3.html')

def crear1 (request):
    datos = {'form' : DescuentosForm()}
    if request.method == 'POST':
        form = DescuentosForm(request.POST)
        if form.is_valid:
            form.save()
            datos['form'] = form
            datos['color'] = "success"
            datos['mensaje'] = "Datos guardados" 
            return redirect(to="tablaPromo")
    return render (request, 'core/crearpromo.html', datos)

def modificarPromo (request, id):
    promo = Descuentos.objects.get(producto=id )
    datos = {"form":DescuentosForm(instance=promo)}
    if request.method == "POST":
        form = DescuentosForm(request.POST, instance=promo)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto modificado!."
            datos['form'] = form
            return redirect(to="tablaPromo")
    return render(request, 'core/modificarpromo.html', datos)

def tablaPromo(request):
    contexto = {'descuentos': Descuentos.objects.all()}
    return render(request, 'core/listapromo.html', contexto)

def eliminar2 (request, id):
    producto = Descuentos.objects.get(producto = id)
    producto.delete()
    return redirect(to="tablaPromo")

def tablaProducto(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, 'core/listadoprodu.html', contexto)

def crear (request):
    datos = {'form' : ProductoForm()}
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid:
            form.save()
            datos['form'] = form
            datos['color'] = "success"
            datos['mensaje'] = "Datos guardados" 
            return redirect(to="tablaProducto")
    return render (request, 'core/crear.html', datos)

def modificar(request, id):
    producto = Producto.objects.get(nombre=id )
    datos = {"form":ProductoForm(instance=producto)}
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto modificado!."
            datos['form'] = form
            return redirect(to="tablaProducto")
    return render(request, 'core/modificar.html', datos)

def eliminar (request, id):
    producto = Producto.objects.get(nombre = id)
    producto.delete()
    return redirect(to="tablaProducto")
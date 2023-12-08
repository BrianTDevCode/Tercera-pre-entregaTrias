from django.shortcuts import render, redirect
from . models import *
from . forms import *
# Create your views here.

def home(req):
    return render(req,'consesionario/index.html')

def search_view(request):
     
    if request.method == "GET":
        form = AutoBuscarFormulario()
        return render(
            request,
            "consesionario/search.html",
            context={"form": form}
        )
    else:
        formulario = AutoBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            autos_filtrados = []
            for auto in Auto.objects.filter(marca=informacion["marca"]):
                autos_filtrados.append(auto)

            contexto = {"Autos": autos_filtrados}
            return render(request, "consesionario/autos_list.html", contexto)

def customers_view(request):
     
     if request.method == "GET":
        form = ClienteFormulario()
        return render(
             request,
             "consesionario/add_customer.html",
             context={"form": form}
         )
     else:
       
         formulario = ClienteFormulario(request.POST)
         if formulario.is_valid():
            informacion = formulario.cleaned_data

         modelo = Cliente(nombre=request.POST['nombre'],apellido=request.POST['apellido'],edad=request.POST['edad'])
         modelo.save()
        
     return redirect("consesionario:index")

def garages_view(request):
     
     if request.method == "GET":
        form = SucursalFormulario()
        return render(
             request,
             "consesionario/add_garage.html",
             context={"form": form}
         )
     else:
       
         formulario = SucursalFormulario(request.POST)
         if formulario.is_valid():
            informacion = formulario.cleaned_data

         modelo = Sucursal(nombre=request.POST['nombre'],direccion=request.POST['direccion'])
         modelo.save()
        
     return redirect("consesionario:index")

def cars_view(request):
     
     if request.method == "GET":
        form = AutoFormulario()
        return render(
             request,
             "consesionario/add_car.html",
             context={"form": form}
         )
     else:
       
         formulario = AutoFormulario(request.POST)
         if formulario.is_valid():
            informacion = formulario.cleaned_data

         modelo = Auto(marca=request.POST['marca'],modelo=request.POST['modelo'],color=request.POST['color'],precio=request.POST['precio'])
         modelo.save()
        
     return redirect("consesionario:index")
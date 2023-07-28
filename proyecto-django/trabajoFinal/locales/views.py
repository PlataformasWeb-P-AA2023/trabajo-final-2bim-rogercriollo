from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import  Barrios, Localcomida, Localrepuestos, Personas
from .forms import  LocalesComidaForm, LocalesRepuestosForm
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .serializer import LocalesComidaSerializer, LocalesRepuestosSerializer, PersonaSerializer, BarrioSerializer
from rest_framework import viewsets, permissions
# def list_locales_comida(request):
#     locales_comida = LocalesComida.objects.all()
#
#     return render(request, 'LocalesComida_list.html', {'locales_comida': locales_comida })


def ingreso(request):

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.data.get("username")
            raw_password = form.data.get("password")
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(ListLocalesComida)
    else:
        form = AuthenticationForm()

    informacion_template = {'form': form}
    return render(request, 'login.html', informacion_template)




def ListLocalesComida(request):
    template_name= "LocalesComida_list.html"
    return render(request, template_name, {'object_list': Localcomida.objects.all()})


def LocalesComida_create(request):
    if request.method == 'POST':
        form = LocalesComidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista-locales-comida")
    else:
        form = LocalesComidaForm()
    return render(request, 'LocalesComida_form.html', {'formulario': form})


@login_required(login_url="login")
def LocalesComida_edit(request, id):
    e = Localcomida.objects.get(pk=id)
    if request.method == 'POST':
        form = LocalesComidaForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return redirect("lista-locales-comida")
    else:
        form = LocalesComidaForm(instance=e)
    return render(request, 'LocalesComida_form.html', {'formulario': form})


@login_required(login_url="login")
def eliminar_LocalesComida(request, id):
    """
    """
    e = Localcomida.objects.get(pk=id)
    e.delete()
    return redirect("lista-locales-comida")






# def list_LocalesRepuestoss(request):
#     LocalesRepuestoss = LocalesRepuestos.objects.all()
#
#     return render(request, 'LocalesRepuestos_list.html', {'LocalesRepuestoss': LocalesRepuestoss,  })
def ListLocalesRepuestos(request):
    template_name = "LocalesRepuestos_list.html"

    return render(request, template_name, {'object_list': Localrepuestos.objects.all()})


def LocalesRepuestos_create(request):
    if request.method == 'POST':
        form = LocalesRepuestosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_loc_repuestos")
    else:
        form = LocalesRepuestosForm()
    return render(request, 'LocalesRepuestos_form.html', {'formulario': form})

@login_required(login_url="/login")
def LocalesRepuestos_edit(request, id):
    e = Localrepuestos.objects.get(pk=id)
    if request.method == 'POST':
        form = LocalesRepuestosForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            return redirect("listar_loc_repuestos")
    else:
        form = LocalesRepuestosForm(instance=e)
    return render(request, 'LocalesRepuestos_form.html', {'formulario': form})

@login_required(login_url="/login")
def eliminar_LocalesRepuestos(request, id):
    """
    """
    e = Localrepuestos.objects.get(pk=id)
    e.delete()
    return redirect("listar_loc_repuestos")

# API VIEWS:

class LocalesComidaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Localcomida.objects.all()
    serializer_class = LocalesComidaSerializer
    permission_classes = [permissions.IsAuthenticated]


class LocalesRepuestosSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Localrepuestos.objects.all()
    serializer_class = LocalesRepuestosSerializer
    permission_classes = [permissions.IsAuthenticated]


class PersonaSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Personas.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]


class BarrioSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Barrios.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]




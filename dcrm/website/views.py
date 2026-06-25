from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib import messages # type: ignore
from .forms import SigupForm, AddRecordForm # type: ignore
from .models import Record # type: ignore

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Has iniciado sesión exitosamente')
            if user.is_staff or user.is_superuser:
                return redirect('home')
            else:
                return redirect('client_home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('home')

    if request.user.is_authenticated:
        if not (request.user.is_staff or request.user.is_superuser):
            return redirect('client_home')

    return render(request, 'home.html', {'records': records})

def login_user(request):
    return redirect('home')

def client_home(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Debes iniciar sesión para acceder al portal del cliente.')
        return redirect('home')
    if request.user.is_staff or request.user.is_superuser:
        return redirect('home')
    return render(request, 'client_home.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SigupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso e inicio de sesión automático')
            return redirect('home')
    else:
        form = SigupForm()
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if not (request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)):
        messages.error(request, 'No tienes permisos de administrador para acceder a esta sección.')
        return redirect('client_home') if request.user.is_authenticated else redirect('home')
    customer_record = get_object_or_404(Record, id=pk)
    return render(request, 'record.html', {'customer_record': customer_record})

def delete_record(request, pk):
    if not (request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)):
        messages.error(request, 'No tienes permisos de administrador para realizar esta acción.')
        return redirect('client_home') if request.user.is_authenticated else redirect('home')
    delete_it = get_object_or_404(Record, id=pk)
    delete_it.delete()
    messages.success(request, 'Registro eliminado exitosamente')
    return redirect('home')

def add_record(request):
    if not (request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)):
        messages.error(request, 'No tienes permisos de administrador para realizar esta acción.')
        return redirect('client_home') if request.user.is_authenticated else redirect('home')
    form = AddRecordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            add_record = form.save(commit=False)
            add_record.user = request.user
            add_record.save()
            messages.success(request, 'Registro agregado exitosamente')
            return redirect('home')
    return render(request, 'add_record.html', {'form': form})

def update_record(request, pk):
    if not (request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser)):
        messages.error(request, 'No tienes permisos de administrador para realizar esta acción.')
        return redirect('client_home') if request.user.is_authenticated else redirect('home')
    update_it = get_object_or_404(Record, id=pk)
    form = AddRecordForm(request.POST or None, instance=update_it)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro actualizado exitosamente')
            return redirect('home')
    return render(request, 'update_record.html', {'form': form})
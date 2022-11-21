from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegistrationForm

def login_view(request):
    """View for Login User"""

    if request.user.is_authenticated:
        return redirect('index')


    if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como {username}")
                return redirect('index')
            
            else:
                print("Usuario es None")
                login_form = AuthenticationForm()
                messages.error(request, "Usuario o contraseña erróneo")
                context = {}
                context['form'] = login_form
                return render(request, 'login.html', context)

    else:
        login_form = AuthenticationForm()
        context = {}
        context['form'] = login_form
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    """View for Login User"""

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, "Registro exitoso")

            return redirect("index")
        
        messages.error(request, "Error en registro. Información inválida")
    
    else:
        form = RegistrationForm()

        context = {}
        context['form'] = form
        return render(request, 'register.html', context)

from django.shortcuts import render, redirect
from django.views import View
from .models import Usuario, Productor
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UsuarioCreationForm, ProductorCreationForm, ProductorLoginForm, UsuarioLoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def indexPro(request):
    return render(request, 'indexpro.html')

class UsuarioLoginView(View):
    def get(self, request):
        form = UsuarioLoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UsuarioLoginForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data.get('correo')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=correo, password=password)
            if user is not None:
                login(request, user)
                return redirect('register')
        return render(request, 'login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

class RegisterView(CreateView):
    form_class = UsuarioCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
    
class ProductorRegisterView(CreateView):
    form_class = ProductorCreationForm
    template_name = 'productor_register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
class ProductorLoginView(LoginView):
    form_class = ProductorLoginForm
    template_name = 'productor_login.html'
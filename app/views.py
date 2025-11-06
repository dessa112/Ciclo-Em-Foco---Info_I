from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
from .models import CicloMenstrual
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from .models import RegistroCiclo
from .models import Dica
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def sair(request):
    logout(request)
    return redirect('/')


def seguranca(request):
    return render(request, 'seguranca.html')


def dicas(request):
    todas_dicas = Dica.objects.all().order_by('-data_criacao')
    return render(request, 'dicas.html', {'dicas': todas_dicas})


##@login_required
def registro(request):
    if request.method == 'POST':
        RegistroCiclo.objects.create(
            usuario=request.user if request.user.is_authenticated else None,
            data_menstruacao=request.POST.get('data_menstruacao'),
            sintomas=request.POST.get('sintomas'),
            atividades=request.POST.get('atividades'),
            observacoes=request.POST.get('observacoes')
        )
        return redirect('registro')

    if request.user.is_authenticated:
        registros = RegistroCiclo.objects.filter(usuario=request.user).order_by('-data_menstruacao')
    else:
        registros = RegistroCiclo.objects.filter(usuario=None).order_by('-data_menstruacao')

    return render(request, 'registro.html', {'registros': registros})

@login_required
def previsao(request):
    ciclo = CicloMenstrual.objects.filter(usuario=request.user).first()
    proxima_data = None

    if ciclo:
        proxima_data = ciclo.ultima_menstruacao + timedelta(days=ciclo.duracao_ciclo)

    context = {
        'proxima_data': proxima_data
    }
    return render(request, 'previsao.html', context)
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
from django.contrib.auth.views import LoginView

class UsuarioLoginView(LoginView):
    template_name = 'login.html'
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
# views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class UsuarioLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        if self.request.user.is_superuser:
            return '/admin/'  # redireciona admin
        return '/'  # redireciona usuário comum
    
from django.shortcuts import render

def previsao(request):
    return render(request, 'previsao.html')

from django.contrib.auth.views import LoginView

class UsuarioLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        if self.request.user.is_superuser:
            return '/admin/'
        return '/'


def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redireciona para login após cadastro
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})
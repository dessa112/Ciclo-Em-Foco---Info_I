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


from django.shortcuts import render

def historico(request):
    return render(request, "historico.html")

def sintomas(request):
    return render(request, "sintomas.html")

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
        return redirect('historico')
    return render(request, "registro.html")

def historico(request):
    registros = RegistroCiclo.objects.filter(
        usuario=request.user if request.user.is_authenticated else None
    ).order_by('-data_menstruacao')
    return render(request, "historico.html", {"registros": registros})

def editar_registro(request, id):
    registro = get_object_or_404(RegistroCiclo, id=id, usuario=request.user)
    if request.method == 'POST':
        registro.data_menstruacao = request.POST.get('data_menstruacao')
        registro.sintomas = request.POST.get('sintomas')
        registro.atividades = request.POST.get('atividades')
        registro.observacoes = request.POST.get('observacoes')
        registro.save()
        return redirect('historico')
    return render(request, "editar_registro.html", {"registro": registro})

def excluir_registro(request, id):
    registro = get_object_or_404(RegistroCiclo, id=id, usuario=request.user)
    registro.delete()
    return redirect('historico')
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

def herpes(request):
    return render(request, "temas/herpes-e-vida-sexual.html")

def libido(request):
    return render(request, "temas/como-aumentar-libido.html")

def sexo_anal(request):
    return render(request, "temas/sexo-anal-iniciantes.html")

def bolinhas(request):
    return render(request, "temas/bolinhas-na-vagina.html")

def atraso(request):
    return render(request, "temas/causas-atraso-menstrual.html")

def teste(request):
    return render(request, "temas/quando-fazer-teste.html")

from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages
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

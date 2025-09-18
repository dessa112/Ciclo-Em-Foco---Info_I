from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from app.views import IndexView, UsuarioLoginView, previsao, registro,dicas, cadastro


urlpatterns = [
    path('admin/', admin.site.urls),  # painel administrativo
    path('', IndexView.as_view(), name='index'),  # página inicial
    path('login/', UsuarioLoginView.as_view(), name='login'),  # login personalizado
    path('registro/', registro, name='registro'),
    path('dicas/', dicas, name='dicas'),
    path('previsao/', previsao, name='previsao'),  # página de previsão do ciclo
    path('cadastro/', cadastro, name='cadastro'),
]


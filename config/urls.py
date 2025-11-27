from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from app.views import (
    IndexView, UsuarioLoginView, previsao, registro, dicas, cadastro, sair,
    seguranca, herpes, libido, sexo_anal, bolinhas, atraso, teste, sintomas, historico,
    editar_registro, excluir_registro   # ✅ adicionados aqui
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', UsuarioLoginView.as_view(), name='login'),
    path('registro/', registro, name='registro'),
    path('dicas/', dicas, name='dicas'),
    path('previsao/', previsao, name='previsao'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout/', sair, name='logout'),
    path('segur/', seguranca, name='seguranca'),

    # Páginas principais
    path("sintomas/", sintomas, name="sintomas"),
    path("historico/", historico, name="historico"),
    path("historico/editar/<int:id>/", editar_registro, name="editar_registro"),
    path("historico/excluir/<int:id>/", excluir_registro, name="excluir_registro"),

    # Temas
    path("herpes-e-vida-sexual/", herpes, name="herpes"),
    path("como-aumentar-libido/", libido, name="libido"),
    path("sexo-anal-iniciantes/", sexo_anal, name="sexo_anal"),
    path("bolinhas-na-vagina/", bolinhas, name="bolinhas"),
    path("causas-atraso-menstrual/", atraso, name="atraso"),
    path("quando-fazer-teste/", teste, name="teste"),
]

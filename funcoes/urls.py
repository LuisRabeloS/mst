from rest_framework.urls import path
from funcoes.views import VerificaIdade, VerificaSessao

urlpatterns = [
    path('verificaidade/<int:idade>/', VerificaIdade.as_view()),
    path('verificasessao/<int:nivel>/', VerificaSessao.as_view()),
]
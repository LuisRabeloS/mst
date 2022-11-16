from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponse
from rest_framework.response import Response
from rest_framework import status

class VerificaIdade(APIView):
    def get(self, request: HttpRequest, idade: int) -> HttpResponse:
        resposta = str
        if (idade>=18):
            return Response(data={"Excelente! Você pode criar uma conta conosco!"}, status=status.HTTP_200_OK)
        else:
            return Response(data={"Menor de idade! Infelizmente você não pode criar conta conosco."}, status= status.HTTP_400_BAD_REQUEST)


class VerificaSessao(APIView):
    def get(self, request: HttpRequest, nivel: int) -> HttpResponse:
        if (nivel==0):
            return Response(data={"Você possui conta free, não é possível agendar sessões"}, status= status.HTTP_400_BAD_REQUEST)
        elif(nivel==1):
            return Response(data={"Você pode agendar 3 sessões"}, status= status.HTTP_200_OK)
        elif(nivel==2):
            return Response(data={"Você pode agendar 5 sessões"}, status= status.HTTP_200_OK)
        elif(nivel==3):
            return Response(data={"Você pode agendar 8 sessões"}, status= status.HTTP_200_OK)
        else:
            return Response(data={"Inválido"}, status= status.HTTP_400_BAD_REQUEST)
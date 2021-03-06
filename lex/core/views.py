from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView

from core.lexical import get_data
from core.syntax_analysis import get_errors
from core.models import Code
from core.serializers import CodeSerializer

class CodeApiView(ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer

    def post(self, request, format=None):
        data = request.data.get("code")
        data = data.replace("\r", "")
        lex = get_data(data)
        syntax_errors = get_errors(data)
        response_data = []
        for token in lex:
            token_data = {
                'type': token.type,
                'value': str(token.value),
                'lineno': token.lineno,
                'position': token.lexpos,
            }
            response_data.append(token_data)
        response_data.append({"syntax_errors" : syntax_errors})
        return Response(response_data, status=status.HTTP_201_CREATED)

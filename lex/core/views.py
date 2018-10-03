from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from core.lexical import get_data


class CodeApiView(APIView):
    
    def post(self, request, format=None):
        data = request.data.get("code")
        lex = get_data(data)
        response_data = []
        for token in lex:
            token_data = {
                'type': token.type,
                'value': str(token.value),
                'lineno': token.lineno,
                'position': token.lexpos,
            }
            response_data.append(token_data)
        return Response(response_data, status=status.HTTP_201_CREATED)

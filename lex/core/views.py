from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView

from core.lexical import get_data

class CodeApiView(APIView):
    
    def post(self, request, format=None):
        data = request.data.get("code")
        lex = get_data(data)
        datas = []
        for token in lex:
            response_data = {
                'type': token.type,
                'value': token.value,
                'lineno': token.lineno,
                'position': token.lexpos
            }
            datas.append(response_data)
        return Response(datas, status=status.HTTP_201_CREATED)

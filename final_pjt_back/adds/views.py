from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


# 환율정보 불러올 함수
@api_view(['GET'])
def exchange_rate(request):

    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={settings.EXCHANGE_KEY}&searchdate=20180102&data=AP01'
    response = requests.get(url)
    data = response.json()

    return Response(data)
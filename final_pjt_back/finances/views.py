from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from .models import Bank, BankOption, DepositProduct, DepositOption, SavingProduct, SavingOption
from .serializers import BankSerializer, BankOptionSerializer, DepositProductSerializer, DepositOptionSerializer, SavingProductSerializer, SavingOptionSerializer

api_key = settings.FINANCE_API_KEY
domain = 'http://finlife.fss.or.kr/finlifeapi'

# 은행, 옵션 목록 저장
@api_view(['GET'])
def save_banks(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    # 은행 목록 순회
    for li in response.get("result").get("baseList"):
        # 은행 데이터 할당
        save_data = {
            'dcls_month': li['dcls_month'],
            'fin_co_no': li['fin_co_no'],
            'kor_co_nm': li['kor_co_nm'],
            'dcls_chrg_man': li['dcls_chrg_man'],
            'homp_url': li['homp_url'],
            'cal_tel': li['cal_tel'],
        }
        # 직렬화
        serializer = BankSerializer(data=save_data)
        # 유효성 검사 후 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 옵션 목록 순회
    for li in response.get("result").get("optionList"):
        fin_co_no = li['fin_co_no']
        area_cd  = li['area_cd']
        area_nm =  li['area_nm']
        # 데이터 변환
        if li['exis_yn'] == 'Y':
            exis_yn = True
        else:
            exis_yn = False
        
        bank = Bank.objects.get(fin_co_no=fin_co_no)

        option = BankOption(bank=bank, fin_co_no=fin_co_no, area_cd=area_cd, area_nm=area_nm, exis_yn=exis_yn)
        option.save()

    return JsonResponse({ 'message': 'okay'})


# 정기예금 상품 목록 및 옵션 목록 저장
@api_view(['GET'])
def save_deposit_products(request):
    url = f'{domain}/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    # 예금 목록 순회
    for li in response.get("result").get("baseList"):
        bank = Bank.objects.get(fin_co_no=li['fin_co_no'])
        # 예금 상품 데이터 할당
        save_data = {
            'bank': bank.pk,
            'dcls_month': li['dcls_month'],
            'fin_co_no': li['fin_co_no'],
            'kor_co_nm': li['kor_co_nm'],
            'fin_prdt_cd': li['fin_prdt_cd'],
            'fin_prdt_nm': li['fin_prdt_nm'],
            'join_way': li['join_way'],
            'mtrt_int': li['mtrt_int'],
            'spcl_cnd': li['spcl_cnd'],
            'join_deny': li['join_deny'],
            'join_member': li['join_member'],
            'etc_note': li['etc_note'],
            'max_limit': li['max_limit'],
            'dcls_strt_day': li['dcls_strt_day'],
            'dcls_end_day': li['dcls_end_day'],
            'fin_co_subm_day': li['fin_co_subm_day'],
        }
        # 직렬화
        serializer = DepositProductSerializer(data=save_data)
        # 유효성 검사 후 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 옵션 목록 순회
    for li in response.get("result").get("optionList"):
        fin_prdt_cd = li['fin_prdt_cd']
        intr_rate_type_nm  = li['intr_rate_type_nm']
        intr_rate =  li['intr_rate']
        intr_rate2 =  li['intr_rate2']
        save_trm =  li['save_trm']
        
        # 결측치 처리
        if not intr_rate:
            intr_rate = -1
        if not intr_rate2:
            intr_rate2 = -1

        product = DepositProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
        option = DepositOption(product=product, fin_prdt_cd=fin_prdt_cd, intr_rate_type_nm=intr_rate_type_nm, intr_rate=intr_rate, intr_rate2=intr_rate2, save_trm=save_trm)
        option.save()

    return JsonResponse({ 'message': 'okay'})


@api_view(['GET'])
def save_saving_products(request):
    url = f'{domain}/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    
    # 적금 상품 목록 순회
    for li in response.get("result").get("baseList"):
        bank = Bank.objects.get(fin_co_no=li['fin_co_no'])
        # 적금 상품 데이터 할당
        save_data = {
            'bank': bank.pk,
            'dcls_month': li['dcls_month'],
            'fin_co_no': li['fin_co_no'],
            'kor_co_nm': li['kor_co_nm'],
            'fin_prdt_cd': li['fin_prdt_cd'],
            'fin_prdt_nm': li['fin_prdt_nm'],
            'join_way': li['join_way'],
            'mtrt_int': li['mtrt_int'],
            'spcl_cnd': li['spcl_cnd'],
            'join_deny': li['join_deny'],
            'join_member': li['join_member'],
            'etc_note': li['etc_note'],
            'max_limit': li['max_limit'],
            'dcls_strt_day': li['dcls_strt_day'],
            'dcls_end_day': li['dcls_end_day'],
            'fin_co_subm_day': li['fin_co_subm_day'],
        }
        # 직렬화
        serializer = SavingProductSerializer(data=save_data)
        # 유효성 검사 후 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    # 옵션 목록 순회
    for li in response.get("result").get("optionList"):
        fin_prdt_cd = li['fin_prdt_cd']
        intr_rate_type_nm  = li['intr_rate_type_nm']
        rsrv_type_nm = li['rsrv_type_nm']
        intr_rate =  li['intr_rate']
        intr_rate2 =  li['intr_rate2']
        save_trm =  li['save_trm']
        
        # 결측치 처리
        if not intr_rate:
            intr_rate = -1
        if not intr_rate2:
            intr_rate2 = -1

        product = SavingProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
        option = SavingOption(product=product, fin_prdt_cd=fin_prdt_cd, intr_rate_type_nm=intr_rate_type_nm, rsrv_type_nm = rsrv_type_nm, intr_rate=intr_rate, intr_rate2=intr_rate2, save_trm=save_trm)
        option.save()

    return JsonResponse({ 'message': 'okay'})
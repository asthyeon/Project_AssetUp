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
topFinGrpNo_list = ['020000', '030200', '030300', '050000', '060000']

# 은행, 옵션 목록 저장
@api_view(['GET'])
def save_companys(request):
    for topFinGrpNo in topFinGrpNo_list:
        pageNo = 1
        max_page_no = 1
        while pageNo <= max_page_no:
            url = f'{domain}/companySearch.json?auth={api_key}&topFinGrpNo={topFinGrpNo}&pageNo={pageNo}'
            response = requests.get(url).json()
            max_page_no = response.get("result").get("max_page_no")
            pageNo += 1
            
            # 은행 목록 순회
            for li in response.get("result").get("baseList"):
                fin_co_no = li['fin_co_no']

                # 이미 존재하는 데이터인지 확인
                if Bank.objects.filter(fin_co_no=fin_co_no).exists():
                    continue  # 이미 존재하면 건너뛰기
                
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
                
                # 이미 존재하는 데이터인지 확인
                if BankOption.objects.filter(
                    fin_co_no=fin_co_no,
                    area_cd=area_cd,
                    area_nm=area_nm
                    ).exists():
                    continue  # 이미 존재하면 건너뛰기
                
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
    for topFinGrpNo in topFinGrpNo_list:
        pageNo = 1
        max_page_no = 1
        while pageNo <= max_page_no:
            url = f'{domain}/depositProductsSearch.json?auth={api_key}&topFinGrpNo={topFinGrpNo}&pageNo={pageNo}'
            response = requests.get(url).json()
            max_page_no = response.get("result").get("max_page_no")
            pageNo += 1
            
            # 예금 목록 순회
            for li in response.get("result").get("baseList"):
                bank = Bank.objects.get(fin_co_no=li['fin_co_no'])
                
                # 이미 존재하는 데이터 패스
                if DepositProduct.objects.filter(fin_prdt_cd=li['fin_prdt_cd']).exists():
                    continue
                
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
                
                # 이미 존재하는 데이터 패스
                if DepositOption.objects.filter(
                    fin_prdt_cd=fin_prdt_cd,
                    intr_rate_type_nm=intr_rate_type_nm,
                    intr_rate=intr_rate,
                    intr_rate2=intr_rate2,
                    save_trm=save_trm).exists():
                    continue
                
                # 결측치 처리
                if not intr_rate:
                    intr_rate = -1
                if not intr_rate2:
                    intr_rate2 = -1

                product = DepositProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
                option = DepositOption(product=product, fin_prdt_cd=fin_prdt_cd, intr_rate_type_nm=intr_rate_type_nm, intr_rate=intr_rate, intr_rate2=intr_rate2, save_trm=save_trm)
                option.save()

    return JsonResponse({ 'message': 'okay'})


# 적금 상품, 옵션 저장
@api_view(['GET'])
def save_saving_products(request):
    for topFinGrpNo in topFinGrpNo_list:
        pageNo = 1
        max_page_no = 1
        while pageNo <= max_page_no:
            url = f'{domain}/savingProductsSearch.json?auth={api_key}&topFinGrpNo={topFinGrpNo}&pageNo={pageNo}'
            response = requests.get(url).json()
            max_page_no = response.get("result").get("max_page_no")
            pageNo += 1
            
            # 적금 상품 목록 순회
            for li in response.get("result").get("baseList"):
                bank = Bank.objects.get(fin_co_no=li['fin_co_no'])
                
                # 중복 데이터 패스
                if SavingProduct.objects.filter(fin_prdt_cd=li['fin_prdt_cd']).exists():
                    continue
                
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
                
                # 중복 데이터 패스
                if SavingOption.objects.filter(
                    fin_prdt_cd=fin_prdt_cd,
                    intr_rate_type_nm=intr_rate_type_nm,
                    rsrv_type_nm=rsrv_type_nm,
                    intr_rate=intr_rate,
                    intr_rate2=intr_rate2,
                    save_trm=save_trm).exists():
                    continue
                
                # 결측치 처리
                if not intr_rate:
                    intr_rate = -1
                if not intr_rate2:
                    intr_rate2 = -1

                product = SavingProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
                option = SavingOption(product=product, fin_prdt_cd=fin_prdt_cd, intr_rate_type_nm=intr_rate_type_nm, rsrv_type_nm = rsrv_type_nm, intr_rate=intr_rate, intr_rate2=intr_rate2, save_trm=save_trm)
                option.save()

    return JsonResponse({ 'message': 'okay'})


# 금융 회사 조회
@api_view(['GET'])
def get_companys(request):
    # 예금 목록 불러오기
    companys = Bank.objects.all()
    seralizer = BankSerializer(companys, many=True)
    return Response(seralizer.data)

# 특정 금융 회사 옵션 조회
@api_view(['GET'])
def get_company_options(request, fin_co_no):
    # 예금 목록 불러오기
    optionlist = BankOption.objects.filter(fin_co_no=fin_co_no)
    seralizer = BankOptionSerializer(optionlist, many=True)
    return Response(seralizer.data)

# 모든 예금 상품 조회
@api_view(['GET'])
def get_deposit_products(request):
    # 예금 목록 불러오기
    products = DepositProduct.objects.all()
    products_contain_options = []    
    for product in products:
        option_list = DepositOption.objects.filter(fin_prdt_cd=product.fin_prdt_cd)
        serializer1 = DepositOptionSerializer(option_list, many=True)
        serializer2 = DepositProductSerializer(product)
        serializer = {
            'deposit_product':serializer2.data,
            'options':serializer1.data
        }
        products_contain_options.append(serializer)

    return Response(products_contain_options)

# 모든 적금 상품 조회
@api_view(['GET'])
def get_saving_products(request):
    # 예금 목록 불러오기
    products = SavingProduct.objects.all()
    products_contain_options = []    
    for product in products:
        option_list = SavingOption.objects.filter(fin_prdt_cd=product.fin_prdt_cd)
        serializer1 = SavingOptionSerializer(option_list, many=True)
        serializer2 = SavingProductSerializer(product)
        serializer = {
            'saving_product':serializer2.data,
            'options':serializer1.data
        }
        products_contain_options.append(serializer)

    return Response(products_contain_options)
    
# 모든 예금 옵션 조회
@api_view(['GET'])
def get_deposit_options(request):
    # 예금 목록 불러오기
    options = DepositOption.objects.all()
    seralizer = DepositOptionSerializer(options, many=True)
    return Response(seralizer.data)

# 단일 예금 상품 조회
@api_view(['GET'])
def get_deposit_product_detail(request, fin_prdt_cd):
    product = DepositProduct.objects.get(fin_prdt_cd=fin_prdt_cd)
    seralizer = DepositProductSerializer(product)
    return Response(seralizer.data)

# 단일 예금 상품의 옵션 조회
@api_view(['GET'])
def get_deposit_product_options(request, fin_prdt_cd):
    optionlist = DepositOption.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionSerializer(optionlist, many=True)
    return Response(serializer.data)

# 적금 상품 목록 조회
@api_view(['GET'])
def saving_products(request):
    # 적금 목록 불러오기
    products = SavingProduct.objects.all()
    seralizer = SavingProductSerializer(products, many=True)
    return Response(seralizer.data)

# 단일 적금 상품 옵션 조회
@api_view(['GET'])
def saving_product_options(request, fin_prdt_cd):
    optionlist = SavingOption.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = SavingOptionSerializer(optionlist, many=True)
    return Response(serializer.data)


# 예금 상품 검색
@api_view(['GET'])
def search_deposit_products(request, fin_co_no, save_trm):
    
    # 예금 목록 불러오기
    if fin_co_no != '전체':
        products = DepositProduct.objects.filter(fin_co_no=fin_co_no)
    else:
        products = DepositProduct.objects.all()
        
    filtered_products = []
    
    for product in products:
        # 옵션 목록 불러오기
        if save_trm:
            option_list = DepositOption.objects.filter(fin_prdt_cd=product.fin_prdt_cd, save_trm=save_trm)
        else:
            option_list = DepositOption.objects.filter(fin_prdt_cd=product.fin_prdt_cd)
        serializer1 = DepositOptionSerializer(option_list, many=True)
        serializer2 = DepositProductSerializer(product)
        serializer = {
            'deposit_product':serializer2.data,
            'options':serializer1.data
        }
        filtered_products.append(serializer)

    return Response(filtered_products)

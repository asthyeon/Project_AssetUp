from django.urls import path
from . import views


urlpatterns = [
    # 금융회사 저장
    path('save-companys/', views.save_companys, name='save_companys'),
    # 예금 상품, 옵션 저장
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    # 적금 상품, 옵션 저장
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    # 연금저축 상품, 옵션 저장
    # path('save-annuity-products/', views.save_annuity_products, name='save_annuity_products'),
    # 주택담보대출 상품, 옵션 저장
    # 전세자금대출 저장
    # 개인신용대출 저장
    
    # 은행 목록 조회
    path('get-companys/', views.get_companys, name='get_companys'),
    # 은행 옵션 조회
    path('get-company-options/<str:fin_co_no>/', views.get_company_options, name='get_company_options'),
    
    # 예금 상품 조회
    path('get-deposit-products/', views.get_deposit_products, name='get_deposit_products'),
    # 예금 옵션 조회
    path('get-deposit-options/', views.get_deposit_options, name='get_deposit_options'),
    
    # 적금 상품 조회
    path('get_saving_products/', views.get_saving_products, name='get_saving_products'),
    
    # 상품 검색
    path('search-deposit-products/<str:fin_co_no>/<int:save_trm>/', views.search_deposit_products, name='search_deposit_products'),
    # 단일 예금 상품 조회
    path('get-deposit-product-detail/<str:fin_prdt_cd>/', views.get_deposit_product_detail, name='get_deposit_product_detail'),
    # 특정 예금 상품 옵션 조회
    path('get-deposit-product-options/<str:fin_prdt_cd>/', views.get_deposit_product_options, name='get_deposit_product_options'),
    
    # 적금 상품 조회
    path('saving-products/', views.saving_products, name='saving_products'),
    # 특정 적금 옵션 조회
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_product_options, name='saving_product_options'),
        
    # 연금 상품 조회
    # 특정 연금 옵션 조회
    # 대출 상품 조회
    # 특정 대출 옵션 조회
]

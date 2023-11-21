from django.urls import path
from . import views


urlpatterns = [
    # 금융회사
    # 저장
    path('save-companys/', views.save_companys, name='save_companys'),
    # 전체 조회
    path('get-companys/', views.get_companys, name='get_companys'),
    # 전체 옵션 조회
    path('get-company-options/<str:fin_co_no>/', views.get_company_options, name='get_company_options'),
    
    # 정기예금
    # 저장
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    # 전체 상품 조회
    path('get-deposit-products/', views.get_deposit_products, name='get_deposit_products'),
    # 전체 옵션 조회
    path('get-deposit-options/', views.get_deposit_options, name='get_deposit_options'),
    # 단일 상품 조회
    path('get-deposit-product-detail/<str:fin_prdt_cd>/', views.get_deposit_product_detail, name='get_deposit_product_detail'),
    # 단일 예금 상품 옵션 조회
    path('get-deposit-product-options/<str:fin_prdt_cd>/', views.get_deposit_product_options, name='get_deposit_product_options'),
    # 전체 상품 검색
    path('search-deposit-products/<str:fin_co_no>/<int:save_trm>/', views.search_deposit_products, name='search_deposit_products'),
    
    # 적금
    # 저장
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    # 전체 상품 조회
    path('get-saving-products/', views.get_saving_products, name='get_saving_products'),
    # 전체 옵션 조회
    path('get-saving-options/<str:fin_prdt_cd>/', views.get_saving_options, name='get_saving_options'),
    # 단일 상품 조회
    path('get-saving-product-detail/<str:fin_prdt_cd>/', views.get_saving_product_detail, name='get_saving_product_detail'),
    # 단일 적금 상품 옵션 조회
    path('get-saving-product-options/<str:fin_prdt_cd>/', views.get_saving_product_options, name='get_saving_product_options'),
    # 전체 상품 검색
    path('search-saving-products/<str:fin_co_no>/<int:save_trm>/', views.search_saving_products, name='search_saving_products'),

    # 연금저축
    # 저장
    path('save-annuity-saving-products/', views.save_annuity_saving_products, name='save_annuity_saving_products'),
    # 전체 상품 조회
    path('get-annuity-saving-products/', views.get_annuity_saving_products, name='get_annuity_saving_products'),
    # 전체 옵션 조회
    path('get-annuity-saving-options/<str:fin_prdt_cd>/', views.get_annuity_saving_options, name='get_annuity_saving_options'),
    # 단일 상품 조회
    path('get-annuity-saving-product-detail/<str:fin_prdt_cd>/', views.get_annuity_saving_product_detail, name='get_annuity_saving_product_detail'),
    # 단일 적금 상품 옵션 조회
    path('get-annuity-saving-product-options/<str:fin_prdt_cd>/', views.get_annuity_saving_product_options, name='get_annuity_saving_product_options'),
    # 전체 상품 검색
    path('search-annuity-saving-products/<str:fin_co_no>/<int:save_trm>/', views.search_annuity_saving_products, name='search_annuity_saving_products'),
    
    # 주택담보 대출
    # 저장
    path('save-mortgage-loan-products/', views.save_mortgage_loan_products, name='save_mortgage_loan_products'),
    # 전체 상품 조회
    path('get-mortgage-loan-products/', views.get_mortgage_loan_products, name='get_mortgage_loan_products'),
    # 전체 옵션 조회
    path('get-mortgage-loan-options/<str:fin_prdt_cd>/', views.get_mortgage_loan_options, name='get_mortgage_loan_options'),
    # 단일 상품 조회
    path('get-mortgage-loan-product-detail/<str:fin_prdt_cd>/', views.get_mortgage_loan_product_detail, name='get_mortgage_loan_product_detail'),
    # 단일 적금 상품 옵션 조회
    path('get-mortgage-loan-product-options/<str:fin_prdt_cd>/', views.get_mortgage_loan_product_options, name='get_mortgage_loan_product_options'),
    # 전체 상품 검색
    path('search-mortgage-loan-products/<str:fin_co_no>/<int:save_trm>/', views.search_mortgage_loan_products, name='search_mortgage_loan_products'),
    
    # 전세자금 대출
    # 저장
    path('save-rent-house-loan-products/', views.save_rent_house_loan_products, name='save_rent_house_loan_products'),
    # 전체 상품 조회
    path('get-rent-house-loan-products/', views.get_rent_house_loan_products, name='get_rent_house_loan_products'),
    # 전체 옵션 조회
    path('get-rent-house-loan-options/<str:fin_prdt_cd>/', views.get_rent_house_loan_options, name='get_rent_house_loan_options'),
    # 단일 상품 조회
    path('get-rent-house-loan-product-detail/<str:fin_prdt_cd>/', views.get_rent_house_loan_product_detail, name='get_rent_house_loan_product_detail'),
    # 단일 적금 상품 옵션 조회
    path('get-rent-house-loan-product-options/<str:fin_prdt_cd>/', views.get_rent_house_loan_product_options, name='get_rent_house_loan_product_options'),
    # 전체 상품 검색
    path('search-rent-house-loan-products/<str:fin_co_no>/<int:save_trm>/', views.search_rent_house_loan_products, name='search_rent_house_loan_products'),
    
    # 신용 대출
    # 저장
    path('save-credit-loan-products/', views.save_credit_loan_products, name='save_credit_loan_products'),
    # 전체 상품 조회
    path('get-credit-loan-products/', views.get_credit_loan_products, name='get_credit_loan_products'),
    # 전체 옵션 조회
    path('get-credit-loan-options/<str:fin_prdt_cd>/', views.get_credit_loan_options, name='get_credit_loan_options'),
    # 단일 상품 조회
    path('get-credit-loan-product-detail/<str:fin_prdt_cd>/', views.get_credit_loan_product_detail, name='get_credit_loan_product_detail'),
    # 단일 적금 상품 옵션 조회
    path('get-credit-loan-product-options/<str:fin_prdt_cd>/', views.get_credit_loan_product_options, name='get_credit_loan_product_options'),
    # 전체 상품 검색
    path('search-credit-loan-products/<str:fin_co_no>/<int:save_trm>/', views.search_credit_loan_products, name='search_credit_loan_products'),
    
]

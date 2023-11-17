from django.urls import path
from . import views


urlpatterns = [
    # 은행 목록 저장
    path('save-banks/', views.save_banks, name='save_banks'),
    # 예금 상품, 옵션 목록 저장
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products'),
    # 적금 상품, 옵션 목록 저장
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
]

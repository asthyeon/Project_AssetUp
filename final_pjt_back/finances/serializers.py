from rest_framework import serializers
from .models import Bank, BankOption
from .models import DepositProduct, DepositOption
from .models import SavingProduct, SavingOption


# 금융회사
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


# 금융회사 옵션
class BankOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankOption
        fields = '__all__'
        read_only_fields = ['bank']


# 예금 상품
class DepositProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'


# 예금 상품 옵션
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields = ['product']


# 적금 상품
class SavingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'


# 적금 상품 옵션
class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields = ['product']

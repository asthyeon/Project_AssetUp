from django.db import models
from django.conf import settings


# 금융회사
class Bank(models.Model):
    dcls_month = models.TextField()             # 공시 제출월[YYYYMM]
    fin_co_no = models.TextField()              # 금융회사코드
    kor_co_nm = models.TextField()              # 금융회사명
    dcls_chrg_man = models.TextField()          # 공시담당자
    homp_url = models.TextField()               # 홈페이지 주소
    cal_tel = models.TextField()                # 콜센터 전화번호


# 금융회사 옵션
class BankOption(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)    # 외래키
    fin_co_no = models.TextField()          # 금융회사코드
    area_cd = models.TextField()            # 지역구분
    area_nm = models.TextField()            # 지역이름
    exis_yn = models.BooleanField()         # 점포 소재 여부


# 예금 상품
class DepositProduct(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)    # 외래키
    dcls_month = models.TextField()             # 공시 제출월[YYYYMM]
    fin_co_no = models.TextField()   # 금융회사코드
    kor_co_nm = models.TextField()              # 금융회사명
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    fin_prdt_nm = models.TextField()            # 금융 상품명
    join_way = models.TextField(null=True)               # 가입방법
    mtrt_int = models.TextField()               # 만기 후 이자율
    spcl_cnd = models.TextField()               # 우대조건
    join_deny = models.IntegerField(choices=((1, '제한 없음'), (2, '서민전용'), (3, '일부제한')))           # 가입제한(1:제한 없음, 2: 서민전용, 3: 일부제한)
    join_member = models.TextField()            # 가입대상
    etc_note = models.TextField()               # 금융 상품 설명
    max_limit = models.IntegerField(null=True)           # 최고한도
    dcls_strt_day = models.TextField()          # 공시 시작일
    dcls_end_day = models.TextField(null=True)           # 공시 종료일
    fin_co_subm_day = models.TextField()        # 금융회사 제출일 [YYYYMMDDHH24MI]


# 예금 상품 옵션
class DepositOption(models.Model):
    product = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)   # 외래키
    fin_prdt_cd = models.TextField()   # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축금리 유형명
    intr_rate = models.FloatField()     # 저축금리
    intr_rate2 = models.FloatField()    # 최고우대금리
    save_trm = models.IntegerField()    # 저축기간 (단위: 개월)


# 적금 상품
class SavingProduct(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)    # 외래키
    dcls_month = models.TextField()             # 공시 제출월[YYYYMM]
    fin_co_no = models.TextField()   # 금융회사코드
    kor_co_nm = models.TextField()              # 금융회사명
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    fin_prdt_nm = models.TextField()            # 금융 상품명
    join_way = models.TextField(null=True)               # 가입방법
    mtrt_int = models.TextField()               # 만기 후 이자율
    spcl_cnd = models.TextField()               # 우대조건
    join_deny = models.IntegerField(choices=((1, '제한 없음'), (2, '서민전용'), (3, '일부제한')))           # 가입제한(1:제한 없음, 2: 서민전용, 3: 일부제한)
    join_member = models.TextField()            # 가입대상
    etc_note = models.TextField()               # 금융 상품 설명
    max_limit = models.IntegerField(null=True)           # 최고한도
    dcls_strt_day = models.TextField()          # 공시 시작일
    dcls_end_day = models.TextField(null=True)           # 공시 종료일
    fin_co_subm_day = models.TextField()        # 금융회사 제출일 [YYYYMMDDHH24MI]


# 적금 상품 옵션
class SavingOption(models.Model):
    product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()   # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)    # 저축금리 유형명
    rsrv_type_nm = models.TextField()   # 적립 유형
    save_trm = models.IntegerField()    # 저축기간 (단위: 개월)
    intr_rate = models.FloatField()     # 저축금리
    intr_rate2 = models.FloatField()    # 최고우대금리


# 연금저축 상품
class AnnuitySavingProduct(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)    # 외래키
    dcls_month = models.TextField()             # 공시 제출월[YYYYMM]
    fin_co_no = models.TextField()   # 금융회사코드
    kor_co_nm = models.TextField()              # 금융회사명
    fin_prdt_cd = models.TextField() # 금융 상품 코드
    fin_prdt_nm = models.TextField()            # 금융 상품명
    join_way = models.TextField(null=True)               # 가입방법
    pnsn_kind = models.TextField()  # 연금종류
    pnsn_kind_nm = models.TextField()   # 연금종류명
    sale_strt_day = models.TextField()  # 판매 개시일
    mntn_cnt = models.TextField()   # 유지건수[단위: 건] 또는 설정액 [단위: 원]
    prdt_type = models.TextField()  # 상품유형
    prdt_type_nm = models.TextField()   # 상품유형명
    avg_prft_rate = models.FloatField()
    dcls_rate = models.FloatField(null=True) # 공시이율 [소수점 2자리]
    guar_rate = models.FloatField(null=True) # 최저 보증이율
    btrm_prft_rate_1 = models.FloatField()  # 과거 수익률1(전년도) [소수점 2자리]
    btrm_prft_rate_2 = models.FloatField()  # 과거 수익률2(전전년도) [소수점 2자리]
    btrm_prft_rate_3 = models.FloatField()  # 과거 수익률3(전전전년도) [소수점 2자리]
    etc = models.TextField(null=True)    # 기타 사항
    sale_co = models.TextField()    # 판매사
    dcls_strt_day = models.TextField()          # 공시 시작일
    dcls_end_day = models.TextField(null=True)           # 공시 종료일
    fin_co_subm_day = models.TextField()        # 금융회사 제출일 [YYYYMMDDHH24MI]


# 연금저축 옵션
class AnnuitySavingOption(models.Model):
    product = models.ForeignKey(AnnuitySavingProduct, on_delete=models.CASCADE)
    dcls_month = models.TextField()
    fin_co_no = models.TextField()
    fin_prdt_cd = models.TextField()
    pnsn_recp_trm = models.TextField()
    pnsn_recp_trm_nm = models.TextField()
    pnsn_entr_age = models.TextField()
    pnsn_entr_age_nm = models.TextField()
    mon_paym_atm = models.TextField()
    mon_paym_atm_nm = models.TextField()
    paym_prd = models.TextField()
    paym_prd_nm = models.TextField()
    pnsn_strt_age = models.TextField()
    pnsn_strt_age_nm = models.TextField()
    pnsn_recp_amt = models.IntegerField()


# 주택담보대출 상품
class MortgageLoanProduct(models.Model):
    pass

# 주택담보대출 옵션
class MortgageLoanOption(models.Model):
    pass

# 전세자금대출 상품
class RentHouseLoanProduct(models.Model):
    pass

# 전세자금대출 옵션
class RentHouseLoanOption(models.Model):
    pass

# 개인신용대출 상품
class CreditLoanProduct(models.Model):
    pass

# 개인신용대출 옵션
class CreditLoanOption(models.Model):
    pass
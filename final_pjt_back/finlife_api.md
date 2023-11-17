# API KEY
- 한국수출입은행 현재환율
  - 0MrXOupfaP4A372K5pslbO76YrWmFrvt
- 전자공시
    - ee76cbfb00c5dc3ee5f34d9a2fbf2002c2fc80df
- 금감원
  - 6274d5007922d6c151bfa2f76ad3d7e8


# 정기예금 API 예제 url json
http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1

# 정기예금 요청 변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) depositProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나

# 정기예금 API 결과 변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd **	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
mtrt_int	만기 후 이자율
spcl_cnd	우대조건
join_deny	가입제한
Ex) 1:제한없음, 2:서민전용, 3:일부제한
join_member	가입대상
etc_note	기타 유의사항
max_limit	최고한도
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
intr_rate_type	저축 금리 유형
intr_rate_type_nm	저축 금리 유형명
save_trm	저축 기간 [단위: 개월]
intr_rate	저축 금리 [소수점 2자리]
intr_rate2	최고 우대금리 [소수점 2자리]

# 적금 API 예제 url
http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1

# 적금 요청 변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) savingProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나

# 적금 API 결과 변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd**	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
mtrt_int	만기 후 이자율
spcl_cnd	우대조건
join_deny	가입제한
Ex) 1:제한없음, 2:서민전용, 3:일부제한
join_member	가입대상
etc_note	기타 유의사항
max_limit	최고한도
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
intr_rate_type	저축 금리 유형
intr_rate_type_nm	저축 금리 유형명
rsrv_type	적립 유형
rsrv_type_nm	적립 유형명
save_trm	저축 기간 [단위: 개월]
intr_rate	저축 금리 [소수점 2자리]
intr_rate2	최고 우대금리 [소수점 2자리]

# 연금저축 API 예제 URL
http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=060000&pageNo=1

# 연금저축 요청 변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) savingProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나

# 연금저축 API 결과 변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd**	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
pnsn_kind	연금종류
pnsn_kind_nm	연금종류명
sale_strt_day	판매 개시일
mntn_cnt	유지건수[단위: 건] 또는 설정액 [단위: 원]
prdt_type	상품유형
prdt_type_nm	상품유형명
dcls_rate	공시이율 [소수점 2자리]
guar_rate	최저 보증이율
btrm_prft_rate_1	과거 수익률1(전년도) [소수점 2자리]
btrm_prft_rate_2	과거 수익률2(전전년도) [소수점 2자리]
btrm_prft_rate_3	과거 수익률3(전전전년도) [소수점 2자리]
etc	기타사항
sale_co	판매사
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
intr_rate_type	저축 금리 유형
intr_rate_type_nm	저축 금리 유형명
rsrv_type	적립 유형
rsrv_type_nm	적립 유형명
save_trm	저축 기간 [단위: 개월]
intr_rate	저축 금리 [소수점 2자리]
intr_rate2	최고 우대금리 [소수점 2자리]


# 금융회사 API 예제 URL
http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={발급받은 인증키}&topFinGrpNo=020000&pageNo=1

# 금융회사 요청 변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) companySearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나

# 금융회사 API 결과 변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사코드
kor_co_nm	금융회사 명
dcls_chrg_man	공시담당자
homp_url	홈페이지주소
cal_tel	콜센터전화번호
options	옵션목록
options	옵션
area_cd	지역구분
area_nm	지역이름
exis_yn	점포소재여부

# 주택담보대출 API
http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

# 주택담보대출 요청 변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) mortgageLoanProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나

# 주택담보대출 API 결과 변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month ***	공시 제출월 [YYYYMM]
fin_co_no ***	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd***	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
loan_inci_expn	대출 부대비용
erly_rpay_fee	중도상환 수수료
dly_rate	연체 이자율
loan_lmt	대출한도
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
mrtg_type	담보유형 코드
mrtg_type_nm	담보유형
rpay_type	대출상환유형 코드
rpay_type_nm	대출상환유형 **
lend_rate_type	대출금리유형 코드
lend_rate_type_nm	대출금리유형
lend_rate_min	대출금리_최저 [소수점 2자리]
lend_rate_max	대출금리_최고 [소수점 2자리]
lend_rate_avg	전월 취급 평균금리 [소수점 2자리]

# 전세자금대출 API
http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

# 전세자금대출 요청 변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) rentHouseLoanProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나

# 전세자금대출 API 결과 변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month ***	공시 제출월 [YYYYMM]
fin_co_no ***	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd***	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
loan_inci_expn	대출 부대비용
erly_rpay_fee	중도상환 수수료
dly_rate	연체 이자율
loan_lmt	대출한도
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
rpay_type	대출상환유형 코드
rpay_type_nm	대출상환유형 **
lend_rate_type	대출금리유형 코드
lend_rate_type_nm	대출금리유형
lend_rate_min	대출금리_최저 [소수점 2자리]
lend_rate_max	대출금리_최고 [소수점 2자리]
lend_rate_avg	전월 취급 평균금리 [소수점 2자리]


# 개인신용대출 API
http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

# 개인신용대출 요청 변수
요청변수 명	요청변수 ID	타입	필수여부	설명 및 예시
서비스명	-	text	필수	* 각 API의 구분자로 사용
Ex) creditLoanProductsSearch
응답방식	-	text	필수	* API호출 후 받을 결과 값 형태 선택.
Ex) xml, json
인증키	auth	text	필수	* 인증키 신청 후 발급받은 인증키(32자리)
Ex)123XXXXXXX45XXXXXXXXX67XXXXXXXC89
권역코드	topFinGrpNo	text	필수	* 금융회사가 속한 권역 코드
Ex) 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
페이지 번호	pageNo	text	필수	* 조회하고자 하는 페이지 번호
Ex) 1, 2, 3
금융회사 코드 또는 명	financeCd	text	선택	* 금융회사 코드 또는 명
Ex) 0010587, 0010588, 0010722, 국민, 상호, 하나

# 개인신용대출 API 결과 변수
result	설명
err_cd		응답코드
err_msg		응답메시지
total_count		총 상품건수
max_page_no		총 페이지 건수 (총 페이지 건수 = 총 상품건수/1회 조회 개수*)
now_page_no		현재 조회 페이지 번호
products	상품목록
product	상품
baseinfo	기본정보
dcls_month **	공시 제출월 [YYYYMM]
fin_co_no **	금융회사 코드
kor_co_nm	금융회사 명
fin_prdt_cd**	금융상품 코드
fin_prdt_nm	금융 상품명
join_way	가입 방법
crdt_prdt_type	대출종류 코드
crdt_prdt_type_nm	대출종류명
cb_name	CB 회사명
dcls_strt_day	공시 시작일
dcls_end_day	공시 종료일
fin_co_subm_day	금융회사 제출일 [YYYYMMDDHH24MI]
options	옵션목록
options	옵션
crdt_lend_rate_type	금리구분 코드
crdt_lend_rate_type_nm	금리구분
crdt_grad_1	900점 초과 [소수점 2자리]
crdt_grad_4	801~900점 [소수점 2자리]
crdt_grad_5	701~800점 [소수점 2자리]
crdt_grad_6	601~700점 [소수점 2자리]
crdt_grad_10	501~600점 [소수점 2자리]
crdt_grad_11	401~500점 [소수점 2자리]
crdt_grad_12	301~400점 [소수점 2자리]
crdt_grad_13	300점 이하 [소수점 2자리]
crdt_grad_avg	평균 금리 [소수점 2자리]


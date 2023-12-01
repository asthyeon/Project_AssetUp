<template>
  <div class="product-type-buttons">
    <button @click="goBack">뒤로가기</button>
  </div>
  <div>
    <h1>금융상품 상세 정보</h1>
    <div v-if="userStore.isLogin" class='product-type-buttons'>
      <div v-if="userProductsArray.some(item => item[1] === financeStore.anniutyProduct[0].product.fin_prdt_cd)">
        <p>이미 구독 중인 상품입니다.</p>
        <button class='product-type-buttons' @click="updateUser(false)">해제하기</button>
      </div>
      <div v-else>
        <!-- 상품 가입페이지로 이동 -->
        <button class='product-type-buttons' @click="goSubscribe(financeStore.anniutyProduct[0].product.fin_prdt_nd)">가입하기</button>
      </div>
    </div>
    <div class="product-info">
      <p class="section-title">상품 정보</p>
      <div class="info-container">
        <div style="padding-left: 50px;">
          <p>공시제출월 : {{ financeStore.anniutyProduct[0].product.dcls_month }}</p>
          <p>금융회사명 : <span class="clickable-text">{{ financeStore.anniutyProduct[0].product.kor_co_nm }}</span></p>
          <p>상품명 : {{ financeStore.anniutyProduct[0].product.fin_prdt_nm }}</p>
          <p>상품 종류 : {{ financeStore.anniutyProduct[0].product.pnsn_kind_nm }}</p>
          <p>상품 유형 : {{ financeStore.anniutyProduct[0].product.prdt_type_nm }}</p>
      </div>
      <div style="padding-right: 50px;">
          <p>평균 수익률 : {{ financeStore.anniutyProduct[0].product.avg_prft_rate }}%</p>
          <p>공시 이율 : {{ financeStore.anniutyProduct[0].product.dcls_rate }}%</p>
          <p>보장 금리 :</p>
          <p v-html="formatSpecialConditions(financeStore.anniutyProduct[0].product.guar_rate)"></p>

        </div>
      </div>
    </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted, computed } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'

const financeStore = useFinanceStore()
const userStore = useUserStore()

const route = useRoute()
const router = useRouter()
const finPrdtCd = ref('')

financeStore.getOneProduct()

// 현재 금융상품코드
finPrdtCd.value = route.params.fin_prdt_cd

// 단일 상품 조회
financeStore.getAnnuitySavingProductDetail(route.params.fin_prdt_cd)
  
// 상품 구독하기
const updateUser = (isSubscribe) => {
    if (isSubscribe) {
        // 가입하기
        userStore.subscribe(financeStore.anniutyProduct[0].product.fin_prdt_cd)
    } else {
        // 해제하기
        userStore.unsubscribe(financeStore.anniutyProduct[0].product.fin_prdt_cd)
    }
    // 유저의 구독 상품 목록 갱신
    userProductsArray.value = userStore.user.financial_products || []
}

// 줄바꿈 함수
const formatSpecialConditions = (data) => {
  const formattedConditions = data.replace('\n', '<br>')
  return formattedConditions
}

// 유저의 구독 상품 목록
const userProductsArray = computed(() => userStore.user.financial_products || [])

// 상품 가입 페이지로 이동
const goSubscribe = (finPrdtCd) => {
    router.push({name:'subscribe', params:{fin_prdt_cd: finPrdtCd}})
}

// 뒤로 가기
const goBack = () => {
    router.back()
}

// 회사 정보 조회
financeStore.getCompanyDetail(financeStore.depositProduct[0].product.fin_co_no)

// 은행 홈페이지로 가기
const goHomepage = function () {
  // 은행 홈페이지 url 확인
  const homepageUrl = financeStore.company?.homp_url

  if (homepageUrl) {
    // 새 탭에서 은행 홈페이지 열기
    window.open(homepageUrl, '_blank')
  } else {
    console.error('은행 홈페이지 url이 없습니다.')
  }
}

</script>
  
<style scoped>
.product-info {
  margin-top: 20px;
}

.section-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 10px;
}

.info-container {
  display: flex;
  justify-content: space-between;
}

.info-container div {
  width: 48%; /* 조정 가능한 너비 */
}

.product-type-buttons {
  margin-bottom: 20px;
}

.product-type-buttons button {
  margin-right: 10px;
  background-color: #2ecc71;
  color: #ffffff;
  padding: 8px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.product-type-buttons button:hover {
  background-color: #27ae60;
}

.clickable-text {
  color: #3498db;
  text-decoration: underline;
  cursor: pointer;
  transition: color 0.3s ease;
}

.clickable-text:hover {
  color: #2980b9;
}

.card-container {
  text-align: center;
}
</style>
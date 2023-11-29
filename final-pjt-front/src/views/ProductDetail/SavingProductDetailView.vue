<template>
  <div class="product-type-buttons">
    <button @click="goBack">뒤로가기</button>
  </div>
  <div>
    <h1>금융상품 상세 정보</h1>
    <div v-if="userStore.isLogin" class='product-type-buttons'>
      <!-- 구독 중인 상품인 경우 -->
      <div v-if="userProductsArray.some(item => item[1] === financeStore.savingProduct[0].product.fin_prdt_cd)">
          <p>이미 구독 중인 상품입니다.</p>
          <button @click="updateUser(false)">해제하기</button>
      </div>
      <!-- 구독할 수 있는 상품인 경우 -->
      <div v-else>
        <!-- 상품 가입페이지로 이동 -->
        <button @click="goSubscribe(financeStore.savingProduct[0].product.fin_prdt_nd)">가입하기</button>
      </div>
    </div>
    <div class="product-info">
      <p class="section-title">상품 정보</p>
      <div class="">
        <p>공시제출월 : {{ financeStore.savingProduct[0].product.dcls_month }}</p>
        <p>금융회사명 : <span class="clickable-text">{{ financeStore.savingProduct[0].product.kor_co_nm }}</span></p>
        <p>상품명 : {{ financeStore.savingProduct[0].product.fin_prdt_nm }}</p>
        <p>가입제한 : {{ JOIN_DENY_CHOICES[financeStore.savingProduct[0].product.join_deny] }}</p>
        <p>가입방법 : {{ financeStore.savingProduct[0].product.join_way }}</p>
        <p>우대조건 :</p>
        <p>{{ financeStore.savingProduct[0].product.spcl_cnd }}</p>
        <p v-html="formatSpecialConditions(financeStore.savingProduct[0].product.spcl_cnd)"></p>
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

// 현재 금융상품코드
finPrdtCd.value = route.params.fin_prdt_cd
// 단일 상품 조회
financeStore.getSavingProductDetail(route.params.fin_prdt_cd)
// 단일 상품의 옵션 목록 조회
financeStore.getSavingProductOptions(route.params.fin_prdt_cd)

// 가입제한 정보
const JOIN_DENY_CHOICES = {
  1: '제한 없음',
  2: '서민전용',
  3: '일부제한',
}

// 우대조건 줄바꿈 함수
const formatSpecialConditions = (spclCnd) => {
const formattedConditions = spclCnd.replace('\n', '<br>')
return formattedConditions
}
// 상품 구독하기
const updateUser = (isSubscribe) => {
if (isSubscribe) {
  // 가입하기
  userStore.subscribe(financeStore.savingProduct[0].product.fin_prdt_cd);
} else {
  // 해제하기
  userStore.unsubscribe(financeStore.savingProduct[0].product.fin_prdt_cd);
}
// 유저의 구독 상품 목록 갱신
userProductsArray.value = userStore.user.financial_products || []
}

// 유저의 구독 상품 목록
const userProductsArray = ref(userStore.user.financial_products || [])

// 상품 가입 페이지로 이동
const goSubscribe = (finPrdtCd) => {
  router.push({name:'subscribe', params:{fin_prdt_cd: finPrdtCd}})
}

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
</style>
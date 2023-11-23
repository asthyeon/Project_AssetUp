<template>
  <div>
    <button @click="goBack">뒤로가기</button>
  </div>
  <div>
    <h1>금융상품 상세 정보</h1>
      <div v-if="userStore.isLogin">
          <div v-if="userProductsArray.includes(financeStore.depositProduct.fin_prdt_cd)" >
              <p>이미 구독 중인 상품입니다.</p>
              <button @click="updateUser(false)">해제하기</button>
          </div>
          <div v-else>
              <p>가입 대상입니다.</p>
              <button @click="updateUser(true)">가입하기</button>
          </div>
      </div>
      <p>상품 정보</p>
      <div>
          <p>공시제출월 : {{ financeStore.depositProduct.dcls_month }}</p>
          <p>금융회사명 : {{ financeStore.depositProduct.kor_co_nm }}</p>
          <p>상품명 : {{ financeStore.depositProduct.fin_prdt_nm }}</p>
          <p>가입제한 : {{ JOIN_DENY_CHOICES[financeStore.depositProduct.join_deny] }}</p>
          <p>가입방법 : {{ financeStore.depositProduct.join_way }}</p>
          <p>우대조건 :</p>
          <p>{{ financeStore.depositProduct.spcl_cnd }}</p>
          <p v-html="formatSpecialConditions(financeStore.depositProduct.spcl_cnd)"></p>
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
financeStore.getDepositProductDetail(route.params.fin_prdt_cd)
// 단일 상품의 옵션 목록 조회
financeStore.getDepositProductOptions(route.params.fin_prdt_cd)

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
    userStore.subscribe(financeStore.depositProduct.fin_prdt_cd)
  } else {
    // 해제하기
    userStore.unsubscribe(financeStore.depositProduct.fin_prdt_cd)
  }
  // 유저의 구독 상품 목록 갱신
  userProductsArray.value = userStore.user.financial_products?.split(',') || []
}

// 유저의 구독 상품 목록
const userProductsArray = computed(() => userStore.user.financial_products?.split(',') || [])

const goBack = () => {
  router.back()
}

</script>

<style scoped>

</style>
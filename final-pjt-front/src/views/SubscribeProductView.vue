<template>
  <div>
    <button @click="goBack">뒤로가기</button>
  </div>
  <div>
    <h1>금융상품 가입 페이지</h1>
    <div>
      <form @submit="userStore.subscribe(financeStore.depositProduct[0].product.fin_prdt_cd, payment)">
        <input type="payment" name="payment" id="payment" v-model="payment">
        <input type="submit" value="가입하기">
      </form>
          <p>공시제출월 : {{ financeStore.depositProduct[0].product.dcls_month }}</p>
          <p>금융회사명 : {{ financeStore.depositProduct[0].product.kor_co_nm }}</p>
          <p>상품명 : {{ financeStore.depositProduct[0].product.fin_prdt_nm }}</p>
          <p>가입제한 : {{ JOIN_DENY_CHOICES[financeStore.depositProduct[0].product.join_deny] }}</p>
          <p>가입방법 : {{ financeStore.depositProduct[0].product.join_way }}</p>
          <p>우대조건 :</p>
          <p>{{ financeStore.depositProduct[0].product.spcl_cnd }}</p>
          <p v-html="formatSpecialConditions(financeStore.depositProduct[0].product.spcl_cnd)"></p>
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

const payment = ref('')

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

// 뒤로가기
const goBack = () => {
  router.back()
}

</script>

<style  scoped>

</style>
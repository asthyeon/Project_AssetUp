<template>
  <div class='product-type-buttons'>
    <button class='product-type-buttons' @click="goBack">뒤로가기</button>
  </div>
  <div class='product-type-buttons'>
    <h1>금융상품 가입 페이지</h1>
    <div class='product-type-buttons'>
        <form @submit.prevent="userStore.subscribe(financeStore.OneProduct.product.fin_prdt_cd, payment)" style="">
          <label for="payment">월 납입금 : </label>
          <input type="payment" name="payment" id="payment" v-model="payment">
          <button class='product-type-buttons'>가입하기</button>
        </form>
          <p>공시제출월 : {{ financeStore.OneProduct.product.dcls_month }}</p>
          <p>금융회사명 : {{ financeStore.OneProduct.product.kor_co_nm }}</p>
          <p>상품명 : {{ financeStore.OneProduct.product.fin_prdt_nm }}</p>
          <p>가입제한 : {{ JOIN_DENY_CHOICES[financeStore.OneProduct.product.join_deny] }}</p>
          <p>가입방법 : {{ financeStore.OneProduct.product.join_way }}</p>
          <p>우대조건 :</p>
          <p>{{ financeStore.OneProduct.product.spcl_cnd }}</p>
          <p v-html="formatSpecialConditions(financeStore.OneProduct.product.spcl_cnd)"></p>
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

financeStore.getAllProducts()
financeStore.getOneProduct(route.params.fin_prdt_cd)

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

</style>
<template>
  <div class="comparison-container">
    <h1>금융상품 비교</h1>

    <!-- 상품 유형 선택 버튼 -->
    <div class="product-type-buttons">
      <!-- 정기예금 -->
      <button @click="changeToDeposit" :class="{ active: productType === 'deposit' }">정기예금</button>

      <!-- 적금 -->
      <button @click="changeToSaving" :class="{ active: productType === 'saving' }">적금</button>

      <!-- 연금 -->
      <button @click="changeToAnnuity" :class="{ active: productType === 'annuity' }">연금</button>

      <!-- 대출 -->
      <button @click="changeToLoan" :class="{ active: productType === 'loan' }">대출</button>
    </div>

    <div v-if="productType === 'deposit'">
        <DepositProductsView />
    </div>
    <div v-else-if="productType === 'saving'">
        <SavingProductsView />
    </div>
    <div v-else-if="productType === 'annuity'">
        <AnnuitySavingProductsView />
    </div>
    <div v-else>
        <LoanProductsView />
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, computed, watch } from 'vue'
import { useFinanceStore } from '@/stores/finance'
import { useRouter } from 'vue-router'

import DepositProductsView from '@/views/ProductView/DepositProductsView.vue'
import SavingProductsView from '@/views/ProductView/SavingProductsView.vue'
import AnnuitySavingProductsView from '@/views/ProductView/AnnuitySavingProductsView.vue'
import LoanProductsView from '@/views/ProductView/LoanProductsView.vue'


const financeStore = useFinanceStore()

onMounted(() => {
  console.log('mounted')
  // 회사 목록 조회
  financeStore.getCompanys()
  // // 적금 상품 목록 조회
  // financeStore.getSavingProducts()
  // // 예금 상품 목록 조회
  // financeStore.getDepositProducts()
  // // 대출
  // financeStore.getLoanProducts()
  // // 검색 상품 목록 조회
  // financeStore.searchDepositProducts()
})

// 회사 옵션
const selectCompany = ref('')    
const selectedTerm = ref('')
const terms = [6, 12, 24, 36]

const router = useRouter()

const productType = ref('deposit')

// 예금 상품
const changeToDeposit = function () {
  productType.value = 'deposit'
  financeStore.searchDepositProducts()
}

// 적금 상품
const changeToSaving = function () {
  productType.value = 'saving'
  financeStore.searchSavingProducts()
}

// 연금 상품
const changeToAnnuity = function () {
  productType.value = 'annuity'
  financeStore.searchAnnuitySavingProducts()
}

// 대출 상품
const changeToLoan = function () {
  console.log(productType.value)
  productType.value = 'loan'
  console.log(productType.value)
  financeStore.searchLoanProducts()
}

</script>

<style scoped>
/* 스타일이 필요한 경우 추가 */
.comparison-container {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  margin-bottom: 20px;
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

table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

table, th, td {
  border: 1px solid #ddd;
}

th, td {
  padding: 12px; /* 행 간격 조절 */
  text-align: left;
}

th {
  background-color: #3498db; /* 첫 행 배경색 */
  color: #ffffff; /* 첫 행 텍스트 색상 */
}

td {
  background-color: #f2f2f2; /* 짝수 행 배경색 */
}

td:nth-child(odd) {
  background-color: #ffffff; /* 홀수 행 배경색 */
}

.pagination {
  margin-top: 20px;
}

.pagination button {
  margin-right: 5px;
}

.pagination button.active {
  font-weight: bold;
}
</style>

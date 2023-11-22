<template>
  <div>
    <!-- 나이, 성별 Top 3 -->
    {{ rankedByAgeGender }}
    {{ top3ProductsA }}
    <div v-for="product in userProductA">
      {{ product.product.fin_prdt_cd }}
    </div>
    <!-- MBTI Top 3 -->
    {{ rankedByMbti }}
    {{ top3ProductsB }}
    <div v-for="product in userProductB">
      {{ product.product.fin_prdt_cd }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRecommendStore } from '@/stores/recommend'
import { useUserStore } from '@/stores/user'
import { useFinanceStore } from '@/stores/finance'

const userStore = useUserStore()
const recommendStore = useRecommendStore()
const financeStore = useFinanceStore()

// 나이, 성별 기준 상품 순위
recommendStore.rankingProdut({'gender': userStore.user.gender, 'age':userStore.user.age})
const rankedByAgeGender = ref(Object.entries(recommendStore.rankedProductsList))
console.log(rankedByAgeGender.value);

// MBTI 기준 상품 순위
recommendStore.rankingProdut({'mbti': userStore.user.mbti})
const rankedByMbti = ref(Object.entries(recommendStore.rankedProductsList))
console.log(rankedByMbti.value);

// 값으로 내림차순 정렬
rankedByAgeGender.value.sort((a, b) => b[1] - a[1])
rankedByMbti.value.sort((a, b) => b[1] - a[1])

// top3 뽑기
const top3ProductsA = ref(rankedByAgeGender.value.slice(0, 3).map(entry => entry[0]))
const top3ProductsB = ref(rankedByMbti.value.slice(0, 3).map(entry => entry[0]))

const allProducts = ref([])
const userProductA = ref([])
const userProductB = ref([])

financeStore.getDepositProducts()
financeStore.getSavingProducts()
financeStore.getAnnuitySavingProducts()

// 모든 상품 정보
allProducts.value = [
  ...financeStore.depositProductList,
  ...financeStore.savingProductList,
  ...financeStore.annuitySavingProductList
]

// 가입한 상품 정보 가져오기
const findProductByCode = function (finPrdtCd) {
  return allProducts.value.find(product => product.product.fin_prdt_cd === finPrdtCd) || null
}

// 가입한 상품 정보 가져오기
userProductA.value = top3ProductsA.value
  .map(finPrdtCd => findProductByCode(finPrdtCd))
  .filter(product => product !== null)
console.log('User Products:', userProductA.value)

userProductB.value = top3ProductsB.value
  .map(finPrdtCd => findProductByCode(finPrdtCd))
  .filter(product => product !== null)
console.log('User Products:', userProductB.value)

</script>

<style scoped>

</style>
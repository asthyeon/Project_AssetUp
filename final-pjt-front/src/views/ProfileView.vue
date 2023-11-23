<template>
  <div>
    <p></p>
    <button @click="goBack">뒤로가기</button>
  </div>
  <div>
    <header>
      <h1>{{ userStore.user.username }} 님의 프로필 페이지</h1>
    </header>

    <div>
      <p><RouterLink :to="{name:'basic-info'}">기본 정보 수정</RouterLink></p>
      <p><RouterLink :to="{name:'protfolio'}">포트폴리오 수정</RouterLink></p>
      <p><RouterLink :to="{name:'recommend'}">상품 추천 받기</RouterLink></p>
    </div>

    <div>
      <div>
        <div>
          <strong>가입 상품 목록</strong>
          <ul v-if="user.financial_products && user.financial_products.length > 0">
            <li v-for="product in userProducts" :key="product.id">
              {{ product.product.fin_prdt_nm }}
            </li>
            <!-- 여기에 1년 간격으로 금액이 커지는 차트 보여주기 -->
          </ul>
        </div>
        <div>
          <strong>가입 상품 금리</strong>
          <ProductChart />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import ProductChart from '@/components/ProductChart.vue'
import { ref, onMounted, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'

const userStore = useUserStore()
const financeStore = useFinanceStore()
const allProducts = ref([])
const userProducts = ref([])

onMounted(async () => {
  await financeStore.getDepositProducts()
  await financeStore.getSavingProducts()
  // 모든 상품 정보
  allProducts.value = [
      ...financeStore.depositProductList,
      ...financeStore.savingProductList
  ]
  // 유저가 가입한 상품명 목록
  const userProductsArray = computed(() => userStore.user.financial_products || [])

  // 가입한 상품 정보 가져오기
  userProducts.value = userProductsArray.value
  .map(item => findProductByCode(item[1]))
  .filter(product => product !== null)
})
  
  const user = ref('')

  user.value = userStore.user
  
  const router = useRouter()
  
  // 가입한 상품 정보 가져오기
  const findProductByCode = function (finPrdtCd) {
    return allProducts.value.find(product => product.product.fin_prdt_cd === finPrdtCd) || null
  }

const goBack = function () {
  router.back()
}

</script>

<style scoped>

</style>
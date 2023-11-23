<template>
  <div>
    <p></p>
    <button @click="goBack">뒤로가기</button>
  </div>
  <div>
    <header>
      <h1>{{ userStore.user.nickname }}님의 프로필</h1>
    </header>
    </div>
    <div class="container">
    <div id="left">
      <p><button @click="change(1)">가입상품</button></p>
      <p><button @click="change(2)">상품추천</button></p>
      <p><button @click="change(3)">기본정보</button></p>
    </div>

    <div id="right">
      <div v-if="status === '1'">
        <ProductView />
      </div>
      <div v-else-if="status === '2'">
        <PortfolioUpdate />
      </div>
      <div v-else>
        <BasicInfoUpdate />
      </div>
    </div>
  </div>
</template>

<script setup>
<<<<<<< HEAD
import ProductChart from '@/components/ProductChart.vue'
=======
import { RouterLink, RouterView } from 'vue-router'
import ProductView from '@/views/ProductView.vue'
>>>>>>> master
import { ref, onMounted, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
<<<<<<< HEAD
=======
import BasicInfoUpdate from '../components/BasicInfoUpdate.vue'
import PortfolioUpdate from '../components/PortfolioUpdate.vue'
>>>>>>> master

const userStore = useUserStore()
const financeStore = useFinanceStore()
const allProducts = ref([])
const userProducts = ref([])
const status = ref('1')

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

const to = 'product'

// 클릭 시 라우터를 조작하는 메소드
const handleRouterLinkClick = () => {
  // 직접 라우터를 조작하여 URL을 변경하지 않고, 라우터뷰에 특정 컴포넌트를 렌더링합니다.
  // 여기에서는 $router.push를 사용했지만 $router.replace 등을 사용할 수 있습니다.
  router.replace({ name: to })
}

const change = (num) => {
  if (num === 1) {
    status.value = '1'
  } else if (num === 2) {
    status.value = '2'
  } else {
    status.value = '3'
  }
}

</script>

<style scoped>
  .container {
    display: grid;
    grid-template-columns: 1fr 4fr;
    gap: 10px; /* 컨테이너 안의 요소들 간의 간격을 조절하세요 */
  }

  #left {
    width: 100px;
  }

  button {
    margin-bottom: 10px; /* 버튼 사이의 간격을 조절하세요 */
    width: 100px;
    padding: 8px; /* 버튼의 내부 여백을 조절하세요 */
    border: none;
    background-color: #3498db; /* 버튼의 배경 색상을 설정하세요 */
    color: #ffffff; /* 버튼 텍스트의 색상을 설정하세요 */
    cursor: pointer;
    transition: background-color 0.3s ease; /* 배경 색상에 변화를 부드럽게 추가합니다 */
  }

  button:hover {
    background-color: #2980b9; /* 마우스를 올렸을 때의 배경 색상을 설정하세요 */
  }

  header {
    text-align: right;
  }

</style>
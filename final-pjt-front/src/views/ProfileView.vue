<template>
  <div>
    <header class="header">
      <h1>{{ userStore.user.nickname }}님의 프로필</h1>
    </header>
    <div class="profile-container">
      <!-- 프로필 텍스트 -->
      <div class="profile-text">
        <!-- 프로필 텍스트 내용을 넣어주세요 -->
      </div>
      <!-- 게이지 -->
      <div class="progress-bar-container">
        <div class="progress">
          <div class="progress-bar" role="progressbar" :aria-valuenow="progress" aria-valuemin="0" :aria-valuemax="100" :style="{ width: progress + '%' }"></div>
        </div>
        <p>{{ progress }}%</p>
      </div>
    </div>
    <div class="container">
      <!-- 왼쪽 메뉴 -->
      <div id="left" class="left-menu">
        <div class="left-menu-buttons">
          <p><button @click="change(1)" class="btn btn-success">가입상품</button></p>
          <p><button @click="change(2)" class="btn btn-success">상품추천</button></p>
          <p><button @click="change(3)" class="btn btn-success">기본정보</button></p>
        </div>
      </div>
      <!-- 오른쪽 컨텐츠 -->
      <div id="right" class="right-content">
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
  </div>
</template>
<script setup>
import { RouterView } from 'vue-router'
import ProductView from '@/views/ProductView.vue'
import PortfolioUpdate from '@/components/PortfolioUpdate.vue'
import BasicInfoUpdate from '@/components/BasicInfoUpdate.vue'
import { ref, onMounted, computed } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'

const userStore = useUserStore()
const financeStore = useFinanceStore()
const allProducts = ref([])
const userProducts = ref([])
const status = ref('1')
const progress = ref(50); // 임의의 값, 실제 값에 따라 변경

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
.header {
  background-color: #ffffff;
  color: #2ecc71;
  padding: 10px;
  text-align: right;
}

.profile-container {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 10px;
}

.profile-text {
  background-color: #f5f5f5;
  padding: 10px;
  border-radius: 5px;
}

.progress-bar-container {
  margin-top: 20px;
}

.progress {
  height: 20px;
}

.container {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 10px;
}

.left-menu {
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 10px;
}

.left-menu-buttons {
  background-color: #f5f5f5;
  border-radius: 5px;
  padding: 10px;
}

.left-menu button {
  width: 100%;
}

.right-content {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
}
</style>
<template>
  <div class="d-flex flex-column profile-container">

    <header class="header">
      <h3>{{ userStore.user.nickname }}님의 프로필</h3>
    </header>

    <div class="profile-text">

      <!-- 게이지 -->
      <div class="progress-bar-container">
        <div class="progress">
          <div class="progress-bar" role="progressbar" :aria-valuenow="calculateProgress" aria-valuemin="0" :aria-valuemax="userStore.user.target_asset" :style="{ width: calculateProgress + '%' }"></div>
        </div>
        <p class="progress-label">{{ calculateProgress.toFixed(2) }}%</p>
      </div>

    </div>

    <div class="container">
      <!-- 왼쪽 메뉴 -->
      <div id="left" class="left-menu">
        <div @click="change(1)" class="left-menu-buttons">가입상품</div>
        <hr>
        <div @click="change(2)" class="left-menu-buttons">상품추천</div>
        <hr>
        <div @click="change(3)" class="left-menu-buttons">기본정보</div>
        <hr>
      </div>

      <!-- 오른쪽 컨텐츠 -->
      <div id="right" class="right-content">
        <div v-if="status === '1'" class="content-section">
          <ProductView />
        </div>
        <div v-else-if="status === '2'" class="content-section">
          <PortfolioUpdate />
        </div>
        <div v-else class="content-section" style="">
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
import { useRecommendStore } from '@/stores/recommend'
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

// 현재 자산과 목표 자산을 가져오기
const currentMoney = ref(userStore.user.money)
const targetAsset = ref(userStore.user.target_asset)

// 현재 상태 계산
const calculateProgress = computed(() => {
  return (currentMoney.value / targetAsset.value) * 100
})


</script>

<style scoped>
.header {
  background-color: #ffffff;
  color: #2ecc71;
  padding: 10px;
  text-align: right;
}
/* 마우스를 올렸을 때 효과 */
.left-menu-buttons:hover {
  background-color: #e0e0e0;
  cursor: pointer;
}

/* 그리드 레이아웃 스타일 */
.profile-container {
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 20px;
}

.container {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 20px;
  margin: auto;
}

.content-section {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

/* 기타 수정 및 추가된 스타일 */
.left-menu-buttons {
  background-color: #f5f5f5;
  border-radius: 5px;
  padding: 10px;
}

.header {
  background-color: #ffffff;
  color: #2ecc71;
  padding: 10px;
  text-align: right;
}

.progress-bar-container {
  margin-top: 20px;
}

.progress {
  height: 20px;
}

/* Bootstrap 스타일 적용 */
.progress-bar {
  border-radius: 10px;
}

.progress-label {
  margin-top: 5px;
  text-align: center;
  font-weight: bold;
}
</style>
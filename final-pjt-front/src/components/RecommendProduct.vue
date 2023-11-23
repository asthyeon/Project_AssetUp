<template>
  <div class="container d-flex flex-column p-2">
    <!-- 상품 추천 -->
    <div class="mb-4">
      <h3>상품 추천</h3>
    </div>
    <!-- 포트폴리오, 추천 카테고리, 상품 추천 -->
    <div class="d-flex">
      <!-- 왼쪽 영역 (카드) -->
      <div class="flex-shrink-0 me-4">
        <!-- 포트폴리오 -->
        <div class="mb-4">
          <div class="fw-bold">포트폴리오</div>
          <div>
            <!-- 포트폴리오 내용이 들어갈 자리 -->
          </div>
        </div>
        <!-- 추천 카테고리 -->
        <div class="mb-4">
          <div class="fw-bold">추천 카테고리</div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" v-model="selectedOptions.age" @change="recommendStore.updateRecommendation(selectedOptions)" />
            <label class="form-check-label">나이</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" v-model="selectedOptions.gender" @change="recommendStore.updateRecommendation(selectedOptions)" />
            <label class="form-check-label">성별</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" v-model="selectedOptions.mbti" @change="recommendStore.updateRecommendation(selectedOptions)" />
            <label class="form-check-label">MBTI</label>
          </div>
          <div class="form-check">
            <input class="form-check-input" type="checkbox" v-model="selectedOptions.salary" @change="recommendStore.updateRecommendation(selectedOptions)" />
            <label class="form-check-label">연봉</label>
          </div>
        </div>
      </div>
      <!-- 오른쪽 영역 (상품 추천) -->
      <div class="flex-grow-1 overflow-auto">
      <div>
        <div class="fw-bold">상품추천</div>
        <!-- 인기 상품들 카드 -->
        <div>
          <!-- 필터링된 상품 출력 -->
          <div v-if="recommendStore.rankedProductsList.length > 0 || isLoading">
            <h4 class="mb-3">추천된 상품</h4>
            <div v-for="product in recommendStore.rankedProductsList" :key="product.product.fin_prdt_cd" class="card mb-3">
              <div class="card-body">
                <strong>{{ product.product.kor_co_nm }}</strong>
                <div>{{ product.product.fin_prdt_nm }}</div>
              </div>
            </div>
          </div>
          <div v-else>
            <p v-if="!isLoading" class="mb-2">추천된 상품이 없습니다.</p>
            <p v-else>데이터를 로딩 중입니다...</p>
          </div>
        </div>
      </div>
    </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRecommendStore } from '@/stores/recommend'
import { useUserStore } from '@/stores/user'
import { useFinanceStore } from '@/stores/finance'
import { useRouter } from 'vue-router'

const userStore = useUserStore()
const recommendStore = useRecommendStore()
const financeStore = useFinanceStore()

const router = useRouter()
financeStore.getAllProducts()

// 선택 옵션
const selectedOptions = ref({
  age: false,
  gender: false,
  mbti: false,
  salary: false,
})

recommendStore.updateRecommendation(selectedOptions)

const goBack = function () {
  router.back()
}

// recommendStore.calculateAssetGrowthRate('WR0001B')
</script>

<style scoped>
/* 스타일이 필요한 경우 추가 */
</style>

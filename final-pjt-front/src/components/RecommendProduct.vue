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
          <!-- ... (이하 동일) -->
        </div>
      </div>
      <!-- 오른쪽 영역 (상품 추천) -->
      <div class="flex-grow-1 overflow-auto">
        <div>
          <div class="fw-bold">상품추천</div>
          <!-- 인기 상품들 카드 -->
          <div>
            <!-- 필터링된 상품 출력 -->
            <div v-if="recommendStore.rankedProductsList.length > 0">
              <h4 class="mb-3">추천된 상품</h4>
              <div v-for="product in recommendStore.rankedProductsList" :key="product?.product?.fin_prdt_cd" class="card mb-3">
                <div class="card-body" v-if="product && product.product" @click="goDetail">
                  <strong>
                    {{ product.product.kor_co_nm }}
                  </strong>
                  <div>
                    {{ product.product.fin_prdt_nm }}
                  </div>
                </div>
              </div>
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

recommendStore.updateRecommendation(selectedOptions.value)

const goBack = function () {
  router.back()
}


</script>

<style scoped>
.overflow-auto {
  max-height: 400px; /* 원하는 높이로 조절하세요 */
}
</style>

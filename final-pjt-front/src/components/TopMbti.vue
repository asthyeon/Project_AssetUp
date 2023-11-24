<template>
  <div class="top-products">
    <!-- MBTI Top 3 -->
    <h2>{{ userStore.user.mbti }} Top 3</h2>
    <div v-for="product in recommendStore.rankedProductsList.slice(0, 3)" :key="product?.product?.fin_prdt_cd" class="card mb-3">
      <div class="card-body" v-if="product && product.product" @click="">
        <strong>
          {{ product.product.kor_co_nm }}
        </strong>
        <div>
          {{ product.product.fin_prdt_nm }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const recommendStore = useRecommendStore()

recommendStore.rankingProduct({ mbti: userStore.user.mbti })

</script>

<style scoped>
.top-products {
  display: flex;
  flex-wrap: wrap;
  gap: 20px; /* 카드 간격 조절 */
  justify-content: center; /* 카드를 수평 중앙 정렬 */
}

.card {
  width: 300px; /* 카드 너비 조절 */
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card-body {
  padding: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.card-body:hover {
  background-color: #f5f5f5;
}

.card-body strong {
  font-size: 1.2em;
}

.card-body div {
  margin-top: 8px;
  color: #555;
}
</style>

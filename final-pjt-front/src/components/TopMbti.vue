<template>
  <div>
    <!-- MBTI Top 3 -->
    <h2>{{ userStore.user.mbti }} Top3</h2>

    <div v-for="product in recommendStore.rankedProductsList">
      {{ product.product.kor_co_nm }}
    </div>

  </div>
</template>

<script setup>
import { useRecommendStore } from '@/stores/recommend'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
const recommendStore = useRecommendStore()

recommendStore.rankingProdut({mbti:userStore.user.mbti})

</script>

<style scoped>

</style>
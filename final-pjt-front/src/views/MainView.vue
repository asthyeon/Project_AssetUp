<template>
  <div>
    <div>자산Up과 함께하는 금융상품 추천 서비스</div>
    <h3>로그인시 환율정보 및 은행검색 이용이 가능합니다.</h3>
    <hr>
    <hr>
    <h3>예금 Top5</h3>
    <div class="container">
      <div 
        v-for="dp in store.topDps"
        :key="dp[0].product.fin_prdt_cd"
      >
        <p>
          {{ dp[0].product.fin_prdt_nm }}
        </p>
      </div>
    </div>
    <hr>
    <h3>적금 Top5</h3>
    <div class="container">
    <div 
      v-for="sp in store.topSps"
      :key="sp[0].product.fin_prdt_cd"
    >
      <p>
        {{ sp[0].product.fin_prdt_nm }}
      </p>
    </div>
  </div>
    <hr>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useHomeStore } from '@/stores/home';

const store = useHomeStore()

onMounted(() => {
  store.getAll()
})

</script>

<style scoped>
  .container {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px; /* 컨테이너 안의 요소들 간의 간격을 조절하세요 */
  }

  #left, #right {
    padding: 10px; /* 왼쪽과 오른쪽 섹션의 여백을 조절하세요 */
  }

</style>
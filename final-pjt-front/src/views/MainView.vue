<template>
  <div>
    <div>자산Up과 함께하는 금융상품 추천 서비스</div>
    <h3>로그인시 환율정보 및 은행검색 이용이 가능합니다.</h3>
    <hr>
    <h3>전체 Top3</h3>
    <div 
      v-for="allp in store.topAllps"
      :key="allp[0].product.fin_prdt_cd"
    >
      <p>
        {{ allp[0].product.fin_prdt_nm }}
      </p>
    </div>
    <hr>
    <h3>예금 Top3</h3>
    <div 
      v-for="dp in store.topDps"
      :key="dp[0].product.fin_prdt_cd"
    >
      <p>
        {{ dp[0].product.fin_prdt_nm }}
      </p>
    </div>
    <hr>
    <h3>적금 Top3</h3>
    <div 
      v-for="sp in store.topSps"
      :key="sp[0].product.fin_prdt_cd"
    >
      <p>
        {{ sp[0].product.fin_prdt_nm }}
      </p>
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

</style>
<template>
  <div>
    <div class="welcome">
      <h3>자산Up과 함께하는 금융상품 추천 서비스</h3>
      <h6>로그인시 환율정보 및 은행검색 이용이 가능합니다.</h6>
    </div>

    <hr class="separator">
    <hr class="separator">

    <div class="outer-container" :style="{ backgroundColor: '#ffffff' }">
      <div class="product-section">
        <h3>예금 Top5</h3>
        <div class="product-container">
          <div
            v-for="dp in store.topDps"
            :key="dp[0].product.fin_prdt_cd"
            class="product-box"
            :style="{ backgroundColor: getRandomColor(0.3), borderColor: getRandomColor(1) }"
          >
            <p>{{ dp[0].product.fin_prdt_nm }}</p>
          </div>
        </div>
      </div>

      <hr class="separator">

      <div class="product-section">
        <h3>적금 Top5</h3>
        <div class="product-container">
          <div
            v-for="sp in store.topSps"
            :key="sp[0].product.fin_prdt_cd"
            class="product-box"
            :style="{ backgroundColor: getRandomColor(0.8), borderColor: getRandomColor(1) }"
          >
            <p>{{ sp[0].product.fin_prdt_nm }}</p>
          </div>
        </div>
      </div>

      <hr class="separator">
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useHomeStore } from '@/stores/home'

const store = useHomeStore()

onMounted(() => {
  store.getAll()
})

const getRandomColor = (opacity) => {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color + (opacity !== undefined ? Math.round(opacity * 255).toString(16) : '');
}
</script>

<style scoped>
.welcome {
  background-color: #f7f7f7;
  padding: 20px;
  text-align: center;
}

.separator {
  border: 2px solid #2ecc71;
  margin: 20px 0;
}

.outer-container {
  background-color: #ffffff;
}

.product-section {
  padding: 20px;
  border-radius: 10px;
  background-color: rgb(232, 230, 230);
  text-align: center;
  margin: 40px 40px;
}

.product-container {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
  padding: 7px;
}

.product-box {
  padding: 15px;
  border-radius: 8px;
  border: 1px solid;
  color: rgb(33, 30, 30);
  transition: background-color 0.3s ease-in-out;
}

.product-box:hover {
  background-color: rgba(39, 174, 96, 0.9);
}
</style>

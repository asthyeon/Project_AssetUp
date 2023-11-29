<template>
  <div>
    <div v-if="!userStore.isLogin" class="header">
      <div class="welcome">
        <h3>자산Up과 함께하는 금융상품 추천 서비스</h3>
        <h6>로그인시 환율정보 및 은행검색 이용이 가능합니다.</h6>
      </div>

      <div class="outer-container" :style="{ backgroundColor: '#ffffff' }">
        <div class="product-section">
          <h3>예금 Top5</h3>
          <div class="product-container">
            <div
              v-for="dp in store.topDps"
              @click="goDetail(dp[0].product.fin_prdt_cd, dp[0].product.fin_prdt_nm)"
              :key="dp[0].product.fin_prdt_cd"
              class="product-box"
              :style="{ backgroundColor: getRandomColor(0.3), borderColor: getRandomColor(1) }"
            >

              <strong>{{ dp[0].product.fin_prdt_nm }}</strong>
              <p>{{ dp[0].product.kor_co_nm }}</p>
              <p>금리 : 연 {{ dp[0].options[0].intr_rate }}%</p>
            </div>
          </div>
        </div>

        <hr class="separator">

        <div class="product-section">
          <h3>적금 Top5</h3>
          <div class="product-container">
            <div
              class="product-box"
              v-for="sp in store.topSps"
              @click="goDetail(sp[0].product.fin_prdt_cd, sp[0].product.fin_prdt_nm)"
              :key="sp[0].product.fin_prdt_cd"
              :style="{ backgroundColor: getRandomColor(0.8), borderColor: getRandomColor(1) }"
            >
              <strong>{{ sp[0].product.fin_prdt_nm }}</strong>
              <p>{{ sp[0].product.kor_co_nm }}</p>
              <p>금리 : 연 {{ sp[0].options[0].intr_rate }}%</p>
            </div>
          </div>
        </div>

        <hr class="separator">
      </div>
    </div>

    <div v-else>
      <div class="welcome">
        <h4><strong>{{ userStore.user.nickname }}</strong>님 어서오세요!<br>오늘도 자산 Up!</h4>
        <div>
          <div class="progress-bar-container">
      <div class="progress">
        <div class="progress-bar" role="progressbar" :aria-valuenow="calculateProgress" aria-valuemin="0" :aria-valuemax="userStore.user.target_asset" :style="{ width: calculateProgress + '%' }">
          <!-- 텍스트를 나타내는 progress-label 추가 -->
          <p class="progress-label">{{ calculateProgress.toFixed(2) }}%</p>
        </div>
      </div>
    </div>
        </div>
      </div>

      <div class="content-container">
        <div class="left-menu">
          <div>
            <TopAgeGender />
          </div>

          <div style="margin-top: 20px;">
            <TopMbti />
          </div>
        </div>

        <div class="right-content">
          <div>
            <SubscribeProduct />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useHomeStore } from '@/stores/home'
import { useUserStore } from '@/stores/user'
import { useRecommendStore } from '@/stores/recommend'
import { useFinanceStore } from '@/stores/finance'
import TopAgeGender from '@/components/TopAgeGender.vue'
import TopMbti from '@/components/TopMbti.vue'
import SubscribeProduct from '@/components/SubscribeProduct.vue'

const router = useRouter()
const store = useHomeStore()
const userStore = useUserStore()
const recommendStore = useRecommendStore()

// 현재 자산과 목표 자산을 가져오기
const currentMoney = ref(userStore.user.money)
const targetAsset = ref(userStore.user.target_asset)

// 현재 상태 계산
const calculateProgress = computed(() => {
  return (currentMoney.value / targetAsset.value) * 100
})

onMounted(() => {
  store.getAll()
})

// 랜덤 색깔 부여
const getRandomColor = (opacity) => {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color + (opacity !== undefined ? Math.round(opacity * 255).toString(16) : '');
}

// 상품 상세 페이지로 이동
const goDetail = function (finPrdtCd, finPrdtNm) {
  if (finPrdtNm.includes('예금')) {
    router.push({name:'deposit_product_detail', params:{fin_prdt_cd: finPrdtCd}})
  } else {
    router.push({name:'saving_product_detail', params:{fin_prdt_cd: finPrdtCd}})
  }
}

</script>

<style scoped>
.welcome {
  background-color: #f7f7f7;
  padding: 20px;
  border-bottom: 10px solid green;
  background-color: white;
  text-align: end;
  height: 150px;
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
.chart-container {
  max-width: 400px; /* 원하는 최대 너비 설정 */
  max-height: 200px; /* 원하는 최대 높이 설정 */
  margin: auto; /* 가운데 정렬을 위한 마진 설정 */
}

.content-container {
  display: flex;
  justify-content: space-between;
}

.left-menu {
  flex: 1;
  padding: 20px;
}

.right-content {
  flex: 3; /* 예시로 3:7 비율로 설정 */
  padding: 20px;
}

.progress-bar-container {
  margin-top: 20px;
  display: flex;
  justify-content: flex-end; /* 내용을 오른쪽으로 정렬 */
}

.progress {
  height: 20px;
  width: 300px;
  position: relative; /* 상대 위치 설정 */
  height: 30px;
}

.progress-bar {
  border-radius: 10px;
  background-color: #05f240; /* 초록색으로 변경 */
}

.progress-label {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* 가운데로 이동시키는 CSS */
  text-align: center;
  font-weight: bold;
  color: black;
}
</style>

<template>
  <div>
    <p></p>
    <button @click="goBack">뒤로가기</button>
  </div>
  <div>
    <header>
      <h1>{{ user.username }} 님의 프로필 페이지</h1>
    </header>

    <div>
      <p>기본 정보 수정</p>
      <RouterLink :to="{name:'protfolio'}">포트폴리오 수정</RouterLink>
      <p>상품 추천 받기</p>
    </div>

    <div>

      <div>
        <h2>기본 정보 수정</h2>
      </div>

      <div>
        <p><strong>회원 번호</strong> : {{ user.id }}</p>
        <p><strong>ID</strong> : {{ user.username }}</p>
        <p>
          <strong>Email</strong> : 
          <span v-if="!user.email">이메일을 수정해주세요</span>
          <span v-else>{{ user.email }}</span>
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>Nickname</strong> : {{ user.nickname }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>나이</strong> : {{ user.age }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>MBTI</strong> : {{ user.mbti }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>주소</strong> : {{ user.address }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>현재 가진 금액</strong> : {{ user.money }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>연봉</strong> : {{ user.salary }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>목표 자산</strong> : {{ user.target_asset }}
          <button @click="goUpdate">수정하기</button>
        </p>

        <div>
          <strong>가입 상품 목록</strong>
          <ul v-if="user.financial_products && user.financial_products.length > 0">
            <li v-for="product in userProducts" :key="product.id">
              {{ product.product.fin_prdt_nm }}
            </li>
            <!-- 여기에 1년 간격으로 금액이 커지는 차트 보여주기 -->
          </ul>
        </div>
        <div>
          <strong>가입 상품 금리</strong>
          <ProductChart />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import ProductChart from '@/components/ProductChart.vue'
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const chartData = ref({
  labels: ['January', 'February', 'March'],
  datasets: [{ data: [40, 20, 12] }],
})

const chartOptions = ref({
  responsive: true,
})

const userStore = useUserStore()
const financeStore = useFinanceStore()
const allProducts = ref([])
const userProducts = ref([])

onMounted(async () => {
  await financeStore.getDepositProducts()
  await financeStore.getSavingProducts()
  // 모든 상품 정보
  allProducts.value = [
      ...financeStore.depositProductList,
      ...financeStore.savingProductList
  ]
  // 유저가 가입한 상품명 목록
  const userProductArray = userStore.user.financial_products.split(',')
  // 가입한 상품 정보 가져오기
  userProducts.value = userProductArray
    .map(finPrdtCd => findProductByCode(finPrdtCd))
    .filter(product => product !== null)
  console.log('User Products:', userProducts.value)
})
  
  const user = ref('')

  user.value = userStore.user
  
  const router = useRouter()
  
  // 회원정보 수정
  const goUpdate = function () {
    router.push({name:'update'})
  }
  
  // 가입한 상품 정보 가져오기
  const findProductByCode = function (finPrdtCd) {
    return allProducts.value.find(product => product.product.fin_prdt_cd === finPrdtCd) || null
  }

const goBack = function () {
  router.back()
}

</script>

<style scoped>

</style>
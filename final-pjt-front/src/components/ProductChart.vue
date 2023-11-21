<template>
  <div>
    <Bar :data="chartData" :options="chartOptions" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { useFinanceStore } from '@/stores/finance'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const chartData = ref({
  labels: [], // x축 상품명
  datasets: [
    {
      label: '저축 금리',
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1,
      data: [],
    },
    {
      label: '최고 우대 금리',
      backgroundColor: 'rgba(192, 75, 192, 0.2)',
      borderColor: 'rgba(192, 75, 192, 1)',
      borderWidth: 1,
      data: [],
    }
  ],
})

const chartOptions = ref({
  responsive: true,
  maintainAspectRatio: true,
  scales: {
    y: {
      beginAtZero: true,
      stepSize: 1,
    },
  },
})

const userStore = useUserStore()
const financeStore = useFinanceStore()
const allProducts = ref([])
const userProducts = ref([])

financeStore.getDepositProducts()
financeStore.getSavingProducts()
// 모든 상품 정보
allProducts.value = [
    ...financeStore.depositProductList,
    ...financeStore.savingProductList
]
// 유저가 가입한 상품명 목록
const userProductArray = userStore.user.financial_products.split(',')

// 가입한 상품 정보 가져오기
const findProductByCode = function (finPrdtCd) {
  return allProducts.value.find(product => product.product.fin_prdt_cd === finPrdtCd) || null
}

// 가입한 상품 정보 가져오기
userProducts.value = userProductArray
  .map(finPrdtCd => findProductByCode(finPrdtCd))
  .filter(product => product !== null)

// 평균 금리 계산하는 함수
const calculateAverageRate = (products) => {
  const totalRate = products.reduce((sum, product) => sum + product.options[0].intr_rate, 0)
  return totalRate / products.length;
}
// 평균 최고 우대 금리 계산하는 함수
const calculateAverageMaxRate = (products) => {
  const totalRate = products.reduce((sum, product) => sum + product.options[0].intr_rate2, 0);
  return totalRate / products.length;
}

// 데이터 가공
const manufactureData = function () {
  // 상품명 추가
  chartData.value.labels.push('평균 금리')
  chartData.value.labels.push(...userProducts.value.map((product) => product.product.fin_prdt_nm))
  
  // 평균 금리 계산
  const averageRate = calculateAverageRate(userProducts.value)
  console.log(averageRate);
  const averageMaxRate = calculateAverageMaxRate(userProducts.value)
  console.log(averageMaxRate);
  chartData.value.datasets[0].data.push(averageRate)
  chartData.value.datasets[1].data.push(averageMaxRate)

  // 각 상품의 저축금리, 최고 우대금리 추가
  userProducts.value.forEach((product) => {
    chartData.value.datasets[0].data.push(product.options[0].intr_rate)
    chartData.value.datasets[1].data.push(product.options[0].intr_rate2)
  })
}


manufactureData()

</script>

<style scoped>

</style>
<template>
  <div>
    <h1>내가 가입한 상품</h1>
    <canvas id="lineChart" width="100" height="100"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Chart, LineController, LinearScale, PointElement, LineElement, CategoryScale } from 'chart.js'
import { useUserStore } from '@/stores/user';
import { useFinanceStore } from '@/stores/finance'
import { useRecommendStore } from '@/stores/recommend';

Chart.register(LineController, LinearScale, PointElement, LineElement, CategoryScale);

const userStore = useUserStore();
const financeStore = useFinanceStore()
const recommendStore = useRecommendStore();

const chartData = ref({
  labels: [],
  datasets: [],
});

const saveTrm = 6;

onMounted(() => {
  financeStore.getAllProducts()
  generateChartData();
  drawLineChart();
});

const generateChartData = () => {
  userStore.user.financial_products.forEach(product => {
    financeStore.getOneProduct(product[1])
    const { intr_rate_type_nm, interestRate, interestRate2 } = recommendStore.calculateAssetGrowthRate(
      product[1],
      saveTrm
    )

    let cumulativeInterest = 0 // 누적 이자를 저장하는 변수 추가

    const interestAmounts = Array.from({ length: saveTrm }, (_, i) => {
      const currentDepositPeriod = i + 1
      const currentInterestRate = intr_rate_type_nm === '단리' ? interestRate : interestRate2
      const monthlyDeposit = product[2]
      const monthlyInterestAmount = monthlyDeposit * (currentInterestRate / 100)
      
      // 누적 이자 계산 및 저장
      cumulativeInterest += monthlyInterestAmount

      return cumulativeInterest
    });

    console.log(financeStore.OneProduct.product.kor_co_nm)
    chartData.value.datasets.push({
      label: financeStore.OneProduct.product.kor_co_nm,
      borderColor: `rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(
        Math.random() * 256
      )}, 1)`,
      borderWidth: 1,
      data: interestAmounts,
    });
  });

  chartData.value.labels = Array.from({ length: saveTrm }, (_, i) => (i + 1) + '개월');
};

const drawLineChart = () => {
  const ctx = document.getElementById('lineChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: chartData.value,
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: {
          beginAtZero: false,
          callback: (value) => `₩${value.toFixed(2)}`, // 통화 기호 및 소수점 2자리까지 표시
        },
        x: {
          type: 'category',
        },
      },
    },
  });
}
</script>

<style scoped>
/* 스타일링을 추가하려면 여기에 작성하세요. */
</style>

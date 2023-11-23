<template>
  <div>
    <h1>내가 가입한 상품</h1>
    <canvas id="lineChart" width="100" height="100"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Chart, LineController, LinearScale, PointElement, LineElement, CategoryScale } from 'chart.js';
import { useUserStore } from '@/stores/user';
import { useRecommendStore } from '@/stores/recommend';

Chart.register(LineController, LinearScale, PointElement, LineElement, CategoryScale);

const userStore = useUserStore();
const recommendStore = useRecommendStore();

const chartData = ref({
  labels: [],
  datasets: [
    {
      label: '이자 금액',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1,
      data: [],
    },
  ],
});

onMounted(() => {
  const financialProduct = userStore.user.financial_products[0]
  drawLineChart(financialProduct[1], 6)
});

console.log(userStore.user);
const drawLineChart = (finPrdtCd, depositPeriod) => {
  const monthlyDeposit = 1000000; // 100만원을 월납입금으로 가정
  chartData.value.labels = Array.from({ length: depositPeriod }, (_, i) => (i + 1) + '개월');

  // 부리 유형과 금리를 가져오는 함수 호출
  const { intr_rate_type_nm, interestRate, interestRate2 } = recommendStore.calculateAssetGrowthRate(finPrdtCd, depositPeriod);

  // 여기서 필요한 comparsionDate를 계산해서 전달
  const comparsionDate = userStore.getCurrentDate();
  const interestAmounts = Array.from({ length: depositPeriod }, (_, i) => {
    const currentDepositPeriod = i + 1;

    // 부리 유형에 따라 금리 선택
    const currentInterestRate = intr_rate_type_nm === '단리' ? interestRate : interestRate2;

    // 월납입금 * 금리
    const monthlyInterestAmount = monthlyDeposit * (currentInterestRate / 100);

    return monthlyInterestAmount * currentDepositPeriod;
  });

  chartData.value.datasets[0].data = interestAmounts;

  new Chart(document.getElementById('lineChart'), {
    type: 'line',
    data: chartData.value,
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        y: {
          beginAtZero: false,
          callback: (value) => `$${value.toFixed(2)}`,
        },
        x: {
          type: 'category',
        },
      },
    },
  });
};
</script>

<style scoped>

</style>

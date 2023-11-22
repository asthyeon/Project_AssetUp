<template>
    <div>

    </div>
</template>

<script setup>
/**
 * 시작 자산을 기준으로 월납입금과 금리를 이용하여 현재 자산을 계산하는 함수
 * @param {number} initialAmount - 시작 자산
 * @param {number} monthlyDeposit - 월납입금
 * @param {number} annualInterestRate - 연간 이자율 (예: 3%를 입력하려면 0.03)
 * @param {number} years - 경과한 년수
 * @returns {number} - 현재 자산
 */
 function calculateFutureValue(initialAmount, monthlyDeposit, annualInterestRate, years) {
  // 연간 이자율을 월 이자율로 변환
  const monthlyInterestRate = annualInterestRate / 12;

  // 총 기간(월) 계산
  const totalMonths = years * 12;

  let futureValue = initialAmount;

  for (let month = 1; month <= totalMonths; month++) {
    // 월 이자 계산
    const interest = futureValue * monthlyInterestRate;

    // 현재 자산 갱신 (현재 자산 + 이자 + 월납입금)
    futureValue = futureValue + interest + monthlyDeposit;
  }

  return futureValue;
}

// 사용 예시
const initialAmount = 10000; // 시작 자산
const monthlyDeposit = 500; // 월납입금
const annualInterestRate = 0.05; // 연간 이자율 (5%)
const years = 10; // 경과한 년수

const currentAmount = calculateFutureValue(initialAmount, monthlyDeposit, annualInterestRate, years);
console.log('현재 자산:', currentAmount);

</script>

<style scoped>

</style>
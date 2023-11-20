<template>
  <div>
    <h1>환율 계산기</h1>
    <hr>
    <select id="currency" v-model="selected">
      <option value="">화폐를 선택하세요</option>
      <option 
        v-for="info in store.exchange_infos"
        :key="info.cur_unit"
        :value="info.cur_unit"
      >
      {{ info.cur_nm }}({{ info.cur_unit }})
      </option>
    </select>
    <div v-if="selected">
      <h2>{{ getExchangeInfo(selected).cur_nm }}({{ getExchangeInfo(selected).cur_unit }})</h2>
      <p>전신환(송금) 받으실 때 : {{ getExchangeInfo(selected).ttb }}</p>
      <p>전신환(송금) 보내실 때: {{ getExchangeInfo(selected).tts }}</p>
      <p>매매 기준율 : {{ getExchangeInfo(selected).deal_bas_r }}</p>
      <h3>환율 계산(매매 기준율)</h3>
      <form @submit.prevent="multiply">
        <label for="number">KRW : </label>
        <input type="text" id="number" v-model="won" @input="validateWon">
        <button type="submit" :disabled="wonError">계산</button>
        <span v-if="wonError" style="color: red;">{{ wonError }}</span>
      </form>
      <form @submit.prevent="multiply2">
        <label for="number">{{ getExchangeInfo(selected).cur_unit }} : </label>
        <input type="text" id="number" v-model="result" @input="validateResult">
        <button type="submit" :disabled="resultError">계산</button>
        <span v-if="resultError" style="color: red;">{{ resultError }}</span>
      </form>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useExchangeStore } from '@/stores/exchange';

const store = useExchangeStore()
const selected = ref('')
const won = ref(null)
const result = ref(null)
const wonError = ref(null)
const resultError = ref(null)

onMounted(() => {
  store.getExchangeRate()
})

const getExchangeInfo = function (cur_unit) {

  return store.exchange_infos.find((info) => info.cur_unit === cur_unit) || {}
}

const formatNumber = function (value) {
  // 정수부와 소수부를 구분하여 ','를 추가하는 함수
  const parts = value.toString().split(".");
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  return parts.join(".");
};

const getNumericExchangeRate = function (rateString) {
  // ',' 제거 후 숫자로 변환
  return parseFloat(rateString.replace(/,/g, ''));
};

// 환율 계산 함수(원 ->)
const multiply = function () {
  resultError.value = null;
  console.log(getExchangeInfo(selected.value).cur_unit);
  if (won.value && selected.value) {
    // 단위가 100인 것들은 100 곱해주기
    if (getExchangeInfo(selected.value).cur_unit === 'IDR(100)') {
      const counting = won.value / Number(getNumericExchangeRate(getExchangeInfo(selected.value).deal_bas_r)) * 100
      console.log(counting);
      result.value = counting.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    } else if (getExchangeInfo(selected.value).cur_unit === 'JPY(100)') {
      const counting = won.value / Number(getNumericExchangeRate(getExchangeInfo(selected.value).deal_bas_r)) * 100
      console.log(counting);
      result.value = counting.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    } else {
      const counting = won.value / Number(getNumericExchangeRate(getExchangeInfo(selected.value).deal_bas_r))
      result.value = counting.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
  } else {
    return null
  }
}

// 환율 계산 함수(-> 원)
const multiply2 = function () {
  console.log(getExchangeInfo(selected.value).cur_unit);
  wonError.value = null;
  if (result.value && selected.value) {
    // 단위가 100인 것들은 100 나눠주기
    if (getExchangeInfo(selected.value).cur_unit === 'IDR(100)') {
      const counting = result.value * Number(getNumericExchangeRate(getExchangeInfo(selected.value).deal_bas_r)) / 100
      console.log(counting);
      won.value = counting.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    } else if (getExchangeInfo(selected.value).cur_unit === 'JPY(100)') {
      const counting = result.value * Number(getNumericExchangeRate(getExchangeInfo(selected.value).deal_bas_r)) / 100
      console.log(counting);
      won.value = counting.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    } else {
      const counting = result.value * Number(getNumericExchangeRate(getExchangeInfo(selected.value).deal_bas_r))
      won.value = counting.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    }
  } else {
    return null
  }
}

// won이 숫자인지 확인
const validateWon = function () {
  if (isNaN(won.value)) {
    wonError.value = '숫자만 입력해주세요.';
  } else {
    wonError.value = null;
  }
}

// result이 숫자인지 확인
const validateResult = function () {
  if (isNaN(result.value)) {
    resultError.value = '숫자만 입력해주세요.';
  } else {
    resultError.value = null;
  }
}

</script>

<style scoped>

</style>
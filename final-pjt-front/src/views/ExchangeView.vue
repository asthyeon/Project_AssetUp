<template>
  <div>
    <h1>환율 계산기</h1>
    <hr>
    <select id="currency" v-model="selected">
      <option disabled value="">화폐를 선택하세요</option>
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
      <h3>환율 계산</h3>
      <label for="number">원(\) : </label>
      <input type="number" id="number" v-model="won">
      <p>결과 : {{ multiply() }}</p>
    </div>
    <div v-for="info in store.exchange_infos">
      <p>{{ info }}</p> 
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useExchangeStore } from '@/stores/exchange';

const store = useExchangeStore()
const selected = ref(null)
const won = ref(null)

onMounted(() => {
  store.getExchangeRate()
})

const getExchangeInfo = function (cur_unit) {
  console.log(store.exchange_infos.find((info) => info.cur_unit === cur_unit));

  return store.exchange_infos.find((info) => info.cur_unit === cur_unit) || {}
}

const multiply = function () {
  if (won.value && selected.value) {
    return won.value * Number(getExchangeInfo(selected.value).deal_bas_r)
  } else {
    return null
  }
}



</script>

<style scoped>

</style>
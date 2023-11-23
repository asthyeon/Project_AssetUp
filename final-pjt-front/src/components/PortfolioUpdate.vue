<template>
  <div>
    <h1>{{ user.nickname }}의 포트폴리오</h1>

    <div>
      <div>연봉 : {{ user.salary }}</div>
      <div>월급 : {{ salary }}</div>
      <p>
        <strong>저축 성향</strong> : 
        <label>
        <input type="radio" v-model="savingsType" value="thrifty"/> 자유형
        </label>
        <label>
        <input type="radio" v-model="savingsType" value="thrifty"/> 근검형
        </label>
        <label>
        <input type="radio" v-model="savingsType" value="challenging"/> 도전형
        </label>
        <label>
        <input type="radio" v-model="savingsType" value="diligent"/> 욜로형
        </label>
        <button @click="goUpdate">수정하기</button>
      </p>
      <p>
        <strong>최애 은행</strong> : 
        <select v-model="favoriteCompany">
          <option v-for="company in financeStore.companys" :key="company.id" :value="company.fin_co_no">{{ company.kor_co_nm }}</option>
        </select>
        <button @click="goUpdate">수정하기</button>
      </p>
      <p>월저축비중 : {{ percent }} %</p>
      <p>월저축금액 : {{ percentMoney }}</p>
      <button @click="updatePercent">월저축비중수정</button>
    </div>
    <hr>
    <div>
      <RecommendProduct />
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useUserStore } from '@/stores/user'
import { useFinanceStore } from '@/stores/finance'
import { useRouter } from 'vue-router'
import axios from 'axios'
import RecommendProduct from './RecommendProduct.vue'

const financeStore = useFinanceStore()
const userStore = useUserStore()
const user = ref('')
user.value = userStore.user
const salary = Math.round(user.value.salary / 12)
const percent = ref(0)
const percentMoney = ref(0)

const router = useRouter()

const savingsType = ref(user.value.saving_type)
const favoriteCompany = ref(user.value.favorite_company)

console.log(user.value)

// 포트폴리오 정보 수정
const goUpdate = function () {
  userStore.updateUserPortfolio(savingsType.value, favoriteCompany.value)
  alert('수정 되었습니다.')
}

const goBack = function () {
  router.back()
}

const updatePercent = () => {
  percent.value = 33
  percentMoney.value = Math.round(salary * percent.value / 100)
}

</script>

<style scoped>

</style>
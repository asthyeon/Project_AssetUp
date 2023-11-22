<template>
  <div>
    <p></p>
    <button @click="goBack">뒤로가기</button>
  </div>
  <div>
    <h1>포트폴리오 수정</h1>

    <div>
      <p><strong>회원 번호</strong> : {{ user.id }}</p>
      <p><strong>ID</strong> : {{ user.username }}</p>
      <p>
        <strong>저축 성향</strong> : 
        <label>
        <input type="radio" v-model="savingsType" value="thrifty"/> 알뜰형
        </label>
        <label>
        <input type="radio" v-model="savingsType" value="challenging"/> 도전형
        </label>
        <label>
        <input type="radio" v-model="savingsType" value="diligent"/> 성실형
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
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useUserStore } from '@/stores/user'
import { useFinanceStore } from '@/stores/finance'
import { useRouter } from 'vue-router'
import axios from 'axios'

const financeStore = useFinanceStore()
const userStore = useUserStore()
const user = ref('')
user.value = userStore.user

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
</script>

<style scoped>

</style>
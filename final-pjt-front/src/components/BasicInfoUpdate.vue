<template>
  <div>
    <p></p>
    <button @click="goBack">뒤로가기</button>
  </div>

  <div>
    
    <div>
      <h2>기본 정보 수정</h2>
    </div>

    <div>
      <p><strong>회원 번호</strong> : {{ userStore.user.id }}</p>
        <p><strong>ID</strong> : {{ userStore.user.username }}</p>
        <p>
          <strong>Email</strong> : 
          <span v-if="!userStore.user.email">이메일을 수정해주세요</span>
          <span v-else>{{ userStore.user.email }}</span>
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>Nickname</strong> : {{ userStore.user.nickname }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>나이</strong> : {{ userStore.user.age }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>MBTI</strong> : {{ userStore.user.mbti }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>주소</strong> : {{ userStore.user.address }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>현재 가진 금액</strong> : {{ userStore.user.money }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>연봉</strong> : {{ userStore.user.salary }}
          <button @click="goUpdate">수정하기</button>
        </p>
        <p>
          <strong>목표 자산</strong> : {{ userStore.user.target_asset }}
          <button @click="goUpdate">수정하기</button>
        </p>
    </div>
  </div>
</template>

<script setup>
import ProductChart from '@/components/ProductChart.vue'
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'
import { useFinanceStore } from '@/stores/finance'
const userStore = useUserStore()
const financeStore = useFinanceStore()
const allProducts = ref([])
const userProducts = ref([])
const router = useRouter()

// 회원정보 수정
const goUpdate = function () {
  router.push({name:'update'})
}
// 뒤로 가기
const goBack = function () {
  router.back()
}
</script>

<style scoped>

</style>
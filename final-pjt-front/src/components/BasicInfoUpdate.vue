<template>
  <div>
    <p></p>
    <button @click="goBack">뒤로가기</button>
  </div>

  <div v-if="status === '1'">
    
    <div>
      <h2>기본정보</h2>
    </div>

    <div>
        <p><strong>아이디</strong> : {{ userStore.user.username }}</p>
        <!-- <p>
          <strong>Email</strong> : 
          <span v-if="!userStore.user.email">이메일을 수정해주세요</span>
          <span v-else>{{ userStore.user.email }}</span>
        </p> -->
        <p>
          <strong>별명</strong> : {{ userStore.user.nickname }}
        </p>
        <p v-if="userStore.user.gender === 'M'">
          <strong>성별</strong> : 남자
        </p>
        <p v-else>
          <strong>성별</strong> : 여자
        </p>

        <p>
          <strong>나이</strong> : {{ userStore.user.age }}
        </p>
        <p>
          <strong>주소</strong> : {{ userStore.user.address }}
        </p>
        <p>
          <strong>연봉</strong> : {{ userStore.user.salary }}
        </p>
        <p>
          <strong>MBTI</strong> : {{ userStore.user.mbti }}
        </p>
        <p>
          <strong>현재자산</strong> : {{ userStore.user.money }}
        </p>
        <p>
          <strong>목표자산</strong> : {{ userStore.user.target_asset }}
        </p>
        <button @click="goUpdate">수정하기</button>
      </div>
    </div>
    <div v-else>
    <h1>기본정보수정</h1>
    <form @submit.prevent="updateUser">
      <!-- <label for="username">아이디 : </label>
      <input type="text" id="username" v-model.trim="user.username"><br>       -->
      <!-- <label for="email"> email : </label>
      <input type="email" id="email" v-model.trim="user.email"><br> -->
      <strong>아이디</strong> : {{ userStore.user.username }}
      <br>
      <label for="nickname">별명 : </label>
      <input type="nickname" id="nickname" v-model.trim="user.nickname"><br>
      <p>성별 : {{ user.gender }}</p>
      <label for="age">나이 : </label>
      <input type="age" id="age" v-model.trim="user.age"><br>
      <label for="address">주소 : </label>
      <input type="address" id="address" v-model.trim="user.address"><br>
      <label for="salary">연봉 : </label>
      <input type="salary" id="salary" v-model.trim="user.salary"><br>
      <label for="mbti">MBTI : </label>
      <input type="mbti" id="mbti" v-model.trim="user.mbti"><br>
      <label for="money">현재자산 : </label>
      <input type="money" id="money" v-model.trim="user.money"><br>
      <label for="target_asset">목표자산 : </label>
      <input type="target_asset" id="target_asset" v-model.trim="user.target_asset"><br>

      <input type="submit" value="수정하기">
    </form>
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
const user = ref(userStore.user)
const status = ref('1')

const gender = ref('')

// 회원정보 수정
const goUpdate = function () {
  status.value = '2'
}
// 뒤로 가기
const goBack = function () {
  router.back()
}

const updateUser = () => {
  status.value = '1'
  userStore.userUpdate({
    // username: user.value.username,
    password: user.value.password,
    // email: user.value.email,
    nickname: user.value.nickname,
    age: user.value.age,
    address: user.value.address,
    salary: user.value.salary,
    money: user.value.money,
    target_asset: user.value.target_asset,
    mbti: user.value.mbti
  })
}
</script>

<style scoped>

</style>
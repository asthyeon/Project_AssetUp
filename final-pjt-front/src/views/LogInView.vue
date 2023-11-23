<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="logIn">
      <label for="username">아이디 </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password">비밀번호</label>
      <input type="password" id="password" v-model.trim="password"><br>
      
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const username = ref(null)
const password = ref(null)

const userStore = useUserStore()

// 로그인 함수
const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  userStore.logIn(payload)
}
</script>

<style scoped>

</style>
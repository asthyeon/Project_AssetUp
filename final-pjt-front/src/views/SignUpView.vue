<template>
  <div>
    <h1>회원가입 페이지</h1>
    <!-- 회원가입 form -->
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username"><br>
      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model.trim="password1"><br>
      <label for="password2">  password confirmation </label>
      <input type="password" id="password2" v-model.trim="password2"><br>
      
      <!-- <label for="email"> email </label>
      <input type="email" id="email" v-model.trim="email"><br> -->
      <label for="nickname"> nickname </label>
      <input type="nickname" id="nickname" v-model.trim="nickname"><br>
      <label for="age"> age </label>
      <input type="age" id="age" v-model.trim="age"><br>
      <label for="address"> address </label>
      <input type="address" id="address" v-model.trim="address"><br>
      <label for="salary"> salary </label>
      <input type="salary" id="salary" v-model.trim="salary"><br>
      <label for="money"> money </label>
      <input type="money" id="money" v-model.trim="money"><br>

      <input type="submit" value="회원가입">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
// const email = ref(null)
const nickname = ref(null)
const age = ref(null)
const address = ref(null)
const salary = ref(null)
const money = ref(null)

const userStore = useUserStore()

// 회원가입 함수
const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value,
    // email: email.value,
    age: age.value,
    address: address.value,
    salary: salary.value,
    money: money.value,
  }
  userStore.signUp(payload)
}

</script>

<style scoped>

</style>
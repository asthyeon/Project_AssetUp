<template>
  <div>
    <h1 class="text-center mb-4 pt-4">로그인</h1>
    <div class="login-container">
      <form @submit.prevent="logIn" class="login-form">
        <label for="username">아이디</label>
        <input class="form-control" type="text" id="username" v-model.trim="username" required>

        <label for="password">비밀번호</label>
        <input class="form-control" type="password" id="password" v-model.trim="password" required>
        <div class="text-center">
          <input type="submit" value="로그인" class="btn btn-success">
        </div>
      </form>
    </div>
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
/* 추가한 스타일 */
.login-container {
  border: 2px solid #4CAF50; /* 초록색 테두리 */
  border-radius: 10px; /* 테두리 둥글게 */
  padding: 20px;
  max-width: 400px;
  margin: 0 auto;
}

/* 기존 스타일 */
.login-form {
  display: grid;
  gap: 10px;
}
</style>

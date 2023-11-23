
<template>
  <header>
    <nav id="app">
      <!-- 메인페이지로 이동 -->
      <RouterLink :to="{name: 'main' }">Home</RouterLink> |
      <!-- 금융상품 비교 페이지로 이동 -->
      <RouterLink :to="{name: 'compare'}">Compare</RouterLink> |
      <!-- 게시판으로 이동 -->
      <RouterLink :to="{name: 'articles' }">Board</RouterLink> |
      <!-- 환율계산기 -->
      <span>
        <RouterLink :to="{name: 'exchange' }">Exchange</RouterLink> |
      </span>
      <!-- 카카오맵 보기 -->
      <span>
        <RouterLink :to="{name: 'map' }">Map</RouterLink> |
      </span>
      <!-- 회원가입 페이지로 이동 -->
      <span v-if="!userStore.isLogin">
        <RouterLink :to="{name: 'signup' }">Signup</RouterLink> |
      </span>
      <!-- 로그인 페이지로 이동 -->
      <span v-if="!userStore.isLogin">
        <RouterLink :to="{name: 'login' }">Login</RouterLink> |
      </span>
      <span v-if="userStore.isLogin" @click="userStore.logOut">Logout | </span>
      <RouterLink v-if="userStore.isLogin" :to="{name: 'profile'}">Profile</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainView from '@/views/MainView.vue'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px; /* Bootstrap navbar height */
}
</style>

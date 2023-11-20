
<template>
  <header>
    <nav>
      <!-- 메인페이지로 이동 -->
      <RouterLink :to="{name: 'main' }">Home</RouterLink> |
      <!-- 금융상품 비교 페이지로 이동 -->
      <RouterLink :to="{name: 'compare'}">Compare</RouterLink> |
      <!-- 게시판으로 이동 -->
      <RouterLink :to="{name: 'articles' }">Board</RouterLink> |
      <!-- 카카오맵 보기 -->
      <RouterLink :to="{name: 'map' }">Map</RouterLink> |
      <!-- 환율계산기 -->
      <RouterLink :to="{name: 'exchange' }">Exchange</RouterLink>
      <!-- 회원가입 페이지로 이동 -->
      <span v-if="!userStore.isLogin">
        | <RouterLink :to="{name: 'signup' }">Signup</RouterLink> |
      </span>
      <!-- 로그인 페이지로 이동 -->
      <span v-if="!userStore.isLogin">
        <RouterLink :to="{name: 'login' }">Login</RouterLink>
      </span>
      | <span @click="userStore.logOut">Logout</span> |
      <RouterLink :to="{name: 'profile'}">Profile</RouterLink>
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

</style>

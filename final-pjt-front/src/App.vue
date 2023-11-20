
<template>
  <header>
    <nav>
      <!-- 메인페이지로 이동 -->
      <RouterLink :to="{name:'main'}">Home</RouterLink> |
      <!-- 금융상품 비교 페이지로 이동 -->
      <RouterLink :to="{name:'compare'}">Compare | </RouterLink>
      <!-- 회원가입 페이지로 이동 -->
      <RouterLink :to="{name:'signup'}" v-if="!userStore.isLogin">Signup | </RouterLink>
      <!-- 로그인 페이지로 이동 -->
      <RouterLink :to="{name:'login'}" v-if="!userStore.isLogin">Login | </RouterLink>
      <!-- 게시판으로 이동 -->
      <RouterLink :to="{name:'board'}">Board | </RouterLink>
      <!-- 카카오맵 보기 -->
      <RouterLink :to="{name:'map'}">Map | </RouterLink>
      <!-- 환율계산기 -->
      <RouterLink :to="{name:'exchange'}">Exchange | </RouterLink>
      <span @click="userStore.logOut">Logout | </span>
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


<template>
  <header>
    <nav>
      <!-- 메인페이지로 이동 -->
      <RouterLink :to="{name:'main'}">Home</RouterLink> |
      <!-- 회원가입 페이지로 이동 -->
      <RouterLink :to="{name:'signup'}" v-if="!userStore.isLogin">Signup | </RouterLink>
      <!-- 로그인 페이지로 이동 -->
      <RouterLink :to="{name:'login'}" v-if="!userStore.isLogin">Login | </RouterLink>
      
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
</script>

<style scoped>

</style>

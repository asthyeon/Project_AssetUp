<template>
  <header>
    <nav id="app">
      <div class="nav-links">
        <!-- 고정된 Home 링크 -->
        <RouterLink :to="{ name: 'main' }" class="nav-link fixed-home">자산Up</RouterLink> |
      </div>
      <div class="auth-links">
        <!-- 금융상품 비교 페이지로 이동 -->
        <RouterLink :to="{ name: 'compare' }" class="nav-link">Compare</RouterLink> |
        <!-- 게시판으로 이동 -->
        <RouterLink :to="{ name: 'articles' }" class="nav-link">Board</RouterLink> |
        <!-- 환율계산기 -->
        <RouterLink :to="{ name: 'exchange' }" class="nav-link">Exchange</RouterLink> |
        <!-- 카카오맵 보기 -->
          <RouterLink :to="{ name: 'map' }" class="nav-link">Map</RouterLink> |
        <!-- 회원가입 페이지로 이동 -->
        <span v-if="!userStore.isLogin" >
          <RouterLink :to="{ name: 'signup' }" class="nav-link">Signup</RouterLink> |
        </span>
        <!-- 로그인 페이지로 이동 -->
        <span v-if="!userStore.isLogin" >
          <RouterLink :to="{ name: 'login' }" class="nav-link">Login</RouterLink> |
        </span>
        <!-- 로그아웃 -->
        <span v-if="userStore.isLogin" @click="userStore.logOut" class="nav-link">Logout | </span>
        <!-- 프로필 페이지로 이동 -->
        <RouterLink v-if="userStore.isLogin" :to="{ name: 'profile' }" class="nav-link">Profile</RouterLink>
      </div>
    </nav>
  </header>
  <body>
    <RouterView />
  </body>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useRecommendStore } from '@/stores/recommend'

const userStore = useUserStore()
const recommendStore = useRecommendStore()

onMounted(() => {
  recommendStore.updateAsset()
})
</script>

<style scoped>
@font-face {
  font-family: 'NanumSquareNeo-Variable';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/NanumSquareNeo-Variable.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}

body {
  font-family: 'NanumSquareNeo-Variable', sans-serif;
  margin: 0;
}

header {
  font-family: 'NanumSquareNeo-Variable', sans-serif;
  background-color: #4CAF50;
  padding: 10px 20px;
  color: white;

}

#app {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links {
  display: flex;
  gap: 10px;
  margin-right: auto; /* 나머지 링크들을 왼쪽으로 붙입니다. */
}

.auth-links {
  display: flex;
  gap: 10px;
}

.nav-link {
  color: white;
  text-decoration: none;
}

.nav-link:hover {
  text-decoration: underline;
}

.fixed-home {
  margin-right: auto;
}
</style>
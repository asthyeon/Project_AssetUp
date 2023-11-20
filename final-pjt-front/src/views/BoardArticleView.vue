<template>
  <div @click="goBack">
    <p>뒤로 가기</p>
  </div>
  <div>
    <h1>게시판</h1>
    <RouterLink :to="{ name: 'board_create' }">
      [CREATE]
    </RouterLink>
    <BoardArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useBoardStore } from '@/stores/board'
import { useRouter, RouterLink } from 'vue-router'
import BoardArticleList from '@/components/BoardArticleList.vue'
import router from '../router';

const store = useBoardStore()

onMounted(() => {
  store.getBoardArticles()
})

const goBack = function () {
  router.back()
}

</script>

<style>

</style>
